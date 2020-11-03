from . import Manager, Fields


class Schedule(Manager):

    def __init__(self, table_name=None):
        Manager.__init__(self, table_name)

    date = Fields().charfield(
        'date',
        10,
        not_null=True
    )

    category = Fields().charfield(
        'category',
        3,
        not_null=True
    )


db_schedule = Schedule()
