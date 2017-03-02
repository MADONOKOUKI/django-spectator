import factory

from . import models


# Factories for core models.

class IndividualCreatorFactory(factory.DjangoModelFactory):
    "A creator that is an individual person."
    class Meta:
        model = models.Creator

    name = factory.Sequence(lambda n: 'Individual %s' % n)
    kind = 'individual'


class GroupCreatorFactory(factory.DjangoModelFactory):
    "A creator that is a group/organisation/etc."
    class Meta:
        model = models.Creator

    name = factory.Sequence(lambda n: 'Group %s' % n)
    kind = 'group'


# Factories for book models.

class BookSeriesFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.BookSeries

    title = factory.Sequence(lambda n: 'Book Series %s' % n)


class BookFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Book

    title = factory.Sequence(lambda n: 'Book %s' % n)
    series = factory.SubFactory(BookSeriesFactory)


class BookRoleFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.BookRole

    role_name = factory.Sequence(lambda n: 'Role %s' % n)
    creator = factory.SubFactory(IndividualCreatorFactory)
    book = factory.SubFactory(BookFactory)


class ReadingFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Reading

    book = factory.SubFactory(BookFactory)


# Factories for event models.

class VenueFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Venue

    name = factory.Sequence(lambda n: 'Venue %s' % n)


class ConcertFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Concert

    title = factory.Sequence(lambda n: 'Concert %s' % n)
    venue = factory.SubFactory(VenueFactory)


class ConcertRoleFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.ConcertRole

    role_name = factory.Sequence(lambda n: 'Role %s' % n)
    creator = factory.SubFactory(IndividualCreatorFactory)
    concert = factory.SubFactory(ConcertFactory)


class MovieFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Movie

    title = factory.Sequence(lambda n: 'Movie %s' % n)


class MovieEventFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.MovieEvent

    movie = factory.SubFactory(MovieFactory)
    venue = factory.SubFactory(VenueFactory)


class MovieRoleFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.MovieRole

    role_name = factory.Sequence(lambda n: 'Role %s' % n)
    creator = factory.SubFactory(IndividualCreatorFactory)
    movie = factory.SubFactory(MovieFactory)

