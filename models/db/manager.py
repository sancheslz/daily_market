from .connector import Connector
from .fields import Fields
from typing import List


class Manager():

    def __init__(self: object, table_name: str = None) -> None:
        self.db = Connector()
        self.db.instance()
        self.db.connect()
        self.table_name = table_name or f'db_{self.__class__.__name__.lower()}'
        self._fields = self.set_fields()

    def set_fields(self: object) -> dict:
        """ Define the table fields """

        return {
            value.field_name: value.is_string for key, value
            in self.__class__.__dict__.items() if not key.startswith('_')
        }

    def create(self: object, *args: list, **kwargs: dict) -> str:
        """ Create table in database """

        message = 'CREATE TABLE {} ({}, {})'.format(
            self.table_name,
            Fields().set_id().sql_constructor,
            ', '.join([
                value.sql_constructor for key, value
                in self.__class__.__dict__.items()
                if not key.startswith('_')
            ])
        )

        try:
            self.db.sql.execute(message)
            self.db.cnc.commit()
            return 'Tabela criada com sucesso'

        except:
            return 'Erro ao criar a tabela, por favor, verifique os parâmetros'

    def insert(self: object, *args: list, **kwargs: dict) -> str:
        """ Insert data into table """

        keys = [value.field_name for key, value in self.__class__.__dict__.items()
                if not key.startswith('_')]
        values = [f"\'{arg}\'" if isinstance(
            arg, str) else str(arg) for arg in args]

        message = "INSERT INTO {} ({}) VALUES ({})".format(
            self.table_name,
            ', '.join(keys),
            ', '.join(values),
        )

        try:
            self.db.sql.execute(message)
            self.db.cnc.commit()
            return 'Dados inseridos com sucesso'
        except:
            return 'Erro ao inserir o dados, por favor, verifique os parâmetros'

    def update(self: object, field: str, new_value: str, condition: str) -> str:
        """ Update data from table """

        message = 'UPDATE {} SET {}={} WHERE {}'.format(
            self.table_name,
            field,
            f"\'{new_value}\'" if self._fields.get(field) else new_value,
            condition
        )

        try:
            self.db.sql.execute(message)
            self.db.cnc.commit()
            return 'Dados atualizados com sucesso'
        except:
            return 'Erro ao atualizar o dados, por favor, verifique os parâmetros'

    def delete(self: object, condition: str) -> str:
        """ Delete date from table """

        message = 'DELETE FROM {} WHERE {}'.format(
            self.table_name,
            condition
        )

        try:
            self.db.sql.execute(message)
            self.db.cnc.commit()
            return 'Dados deletados com sucesso'
        except:
            return 'Erro ao deletar o dados, por favor, verifique os parâmetros'

    def show_all(self: object) -> List[tuple]:
        """ Return all records in table """

        query = self.db.execute(f'SELECT * FROM {self.table_name}').fetchall()
        return query

    def get(self: object, condition: str, *field_list: list) -> List[tuple]:
        """ Get an specific record from table """

        message = 'SELECT {} FROM {} WHERE {}'.format(
            ', '.join(field_list) if len(field_list) != 0 else '*',
            self.table_name,
            condition
        )
        return self.db.sql.execute(message).fetchall()

    def fields(self: object) -> str:
        """ Display all table fields """

        data = [
            str(value.field_name) for key, value
            in self.__class__.__dict__.items() if not key.startswith('_')]

        return f'\n{self.table_name}\n - ' + '\n - '.join(data)+'\n'
