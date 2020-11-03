class Fields():

    def __init__(self: object) -> None:
        self.field_name = None
        self.sql_constructor = None
        self.is_string = False

    def _constructor_helper(self: object, **kwargs: dict) -> list:
        """ Define the SQL optional structure """

        return [
            option for option in [
                'NOT NULL' if kwargs['not_null'] else None,
                'UNIQUE' if kwargs['unique'] else None,
                'DEFAULT {}'.format(
                    f"\"{kwargs.get('default')}\"" if isinstance(
                        kwargs.get('default'), str) else kwargs.get('default')
                ) if kwargs['default'] else None
            ] if option != None
        ]

    def set_id(self: object) -> object:
        """ Default structure for id """

        self.field_name = "id"
        self.sql_constructor = "id INTEGER PRIMARY KEY AUTOINCREMENT"
        return self

    def charfield(self: object, field_name: str, max_length: int = 60,
                  *, not_null: bool = False, unique: bool = None,
                  default: bool = None) -> object:
        """ Define a charfield structure """

        self.field_name = field_name
        self.is_string = True
        options = self._constructor_helper(
            not_null=not_null, unique=unique, default=default
        )

        self.sql_constructor = "{} VARCHAR({}){}".format(
            field_name,
            max_length,
            ' ' + ' '.join(options) if len(options) != 0 else ''
        )
        return self

    def integer(self: object, field_name: str, *, not_null: bool = False,
                unique: bool = None, default: bool = None) -> object:
        """ Define an integer structure """

        self.field_name = field_name

        options = self._constructor_helper(
            not_null=not_null, unique=unique, default=default
        )

        self.sql_constructor = "{} INTEGER{}".format(
            field_name,
            ' ' + ' '.join(options) if len(options) != 0 else ''
        )
        return self

    def boolean(self: object, field_name: str, *, not_null: bool = False,
                unique: bool = None, default: bool = None) -> object:
        """ Define a boolean structure """

        self.field_name = field_name
        options = self._constructor_helper(
            not_null=not_null, unique=unique, default=default
        )

        self.sql_constructor = "{} BOOLEAN{}".format(
            field_name,
            ' ' + ' '.join(options) if len(options) != 0 else ''
        )
        return self

    def foreign_key(self: object, field_name: str,
                    ref_table: object, ref_column: str) -> object:
        """ Define a foreign key structure """

        self.field_name = field_name
        self.sql_constructor = "FOREIGN KEY({}) REFERENCES {}({})".format(
            field_name,
            ref_table,
            ref_column
        )
        return self
