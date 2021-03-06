from . import Manager, Fields


class News(Manager):

    def __init__(self, table_name=None):
        Manager.__init__(self, table_name)

    title = Fields().charfield(
        'title',
        100,
        not_null=True
    )

    date = Fields().charfield(
        'date',
        10,
        not_null=True
    )

    url = Fields().charfield(
        'url',
        200,
        not_null=True
    )


db_news = News()
