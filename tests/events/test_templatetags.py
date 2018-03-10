from django.test import TestCase

from .. import make_date
from spectator.core.factories import IndividualCreatorFactory
from spectator.events.factories import (
    EventRoleFactory, GigEventFactory, CinemaEventFactory, TheatreEventFactory
)
from spectator.events.models import Event
from spectator.events.templatetags.spectator_events import (
    annual_event_counts, day_events, day_events_card, event_list_tabs,
    events_years, events_years_card,
    most_seen_creators, most_seen_creators_card,
    recent_events, recent_events_card
)


class AnnualEventCountsTestCase(TestCase):

    def setUp(self):
        super().setUp()
        CinemaEventFactory.create_batch(1, date=make_date('2015-01-01'))
        GigEventFactory.create_batch(2, date=make_date('2015-06-01'))

        TheatreEventFactory.create_batch(1, date=make_date('2017-01-01'))

        GigEventFactory.create_batch(1, date=make_date('2018-01-01'))
        TheatreEventFactory.create_batch(1, date=make_date('2018-01-01'))

    def test_all(self):
        qs = annual_event_counts()

        self.assertEqual(len(qs), 3)
        self.assertEqual(qs[0],
                    {'year': make_date('2015-01-01'), 'total': 3})
        self.assertEqual(qs[1],
                    {'year': make_date('2017-01-01'), 'total': 1})
        self.assertEqual(qs[2],
                    {'year': make_date('2018-01-01'), 'total': 2})

    def test_kind(self):
        qs = annual_event_counts(kind='gig')

        self.assertEqual(len(qs), 2)
        self.assertEqual(qs[0],
                    {'year': make_date('2015-01-01'), 'total': 2})
        self.assertEqual(qs[1],
                    {'year': make_date('2018-01-01'), 'total': 1})


class EventListTabsTestCase(TestCase):

    def test_result(self):
        counts = {'all': 30, 'gig': 12, 'movie': 18,}
        result = event_list_tabs(counts, 'gig', 2)
        self.assertEqual(result['counts'], counts)
        self.assertEqual(result['current_kind'], 'gig')
        self.assertEqual(result['page_number'], 2)
        self.assertEqual(
            sorted(result['event_kinds']),
            sorted(Event.get_kinds())
        )
        self.assertEqual(
            sorted(result['event_kinds_data'].keys()),
            sorted(Event.get_kinds_data().keys())
        )


class RecentEventsTestCase(TestCase):

    def test_queryset(self):
        "It should return 10 recent events by default."
        CinemaEventFactory.create_batch(6, date=make_date('2017-02-10'))
        GigEventFactory.create_batch(6,    date=make_date('2017-02-12'))
        qs = recent_events()
        self.assertEqual(len(qs), 10)
        self.assertEqual(qs[5].kind, 'gig')
        self.assertEqual(qs[6].kind, 'cinema')

    def test_queryset_num(self):
        "It should return the number of events requested."
        GigEventFactory.create_batch(6, date=make_date('2017-02-12'))
        qs = recent_events(5)
        self.assertEqual(len(qs), 5)


class RecentEventsCardTestCase(TestCase):

    def test_result(self):
        GigEventFactory.create_batch(6, date=make_date('2017-02-12'))
        result = recent_events_card(5)
        self.assertEqual(result['card_title'], 'Recent events')
        self.assertEqual(len(result['event_list']), 5)


class DayEventsTestCase(TestCase):

    def test_queryset(self):
        GigEventFactory(  date=make_date('2017-02-09'))
        CinemaEventFactory(date=make_date('2017-02-10'))
        GigEventFactory(  date=make_date('2017-02-10'))
        CinemaEventFactory(date=make_date('2017-02-11'))
        qs = day_events(make_date('2017-02-10'))
        self.assertEqual(len(qs), 2)


class DayEventsCardTestCase(TestCase):

    def test_result(self):
        GigEventFactory(  date=make_date('2017-02-09'))
        CinemaEventFactory(date=make_date('2017-02-10'))
        GigEventFactory(  date=make_date('2017-02-10'))
        CinemaEventFactory(date=make_date('2017-02-11'))
        result = day_events_card(make_date('2017-02-10'))
        self.assertEqual(result['card_title'], 'Events on 10 Feb 2017')
        self.assertEqual(len(result['event_list']), 2)


class EventsYearsTestCase(TestCase):

    def test_result(self):
        GigEventFactory(  date=make_date('2017-02-09'))
        CinemaEventFactory(date=make_date('2017-02-10'))
        GigEventFactory(  date=make_date('2015-02-09'))
        result = events_years()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], make_date('2015-01-01'))
        self.assertEqual(result[1], make_date('2017-01-01'))


class EventsYearsCardTestCase(TestCase):

    def test_result(self):
        GigEventFactory(  date=make_date('2017-02-09'))
        CinemaEventFactory(date=make_date('2017-02-10'))
        GigEventFactory(  date=make_date('2015-02-09'))
        result = events_years_card(make_date('2017-01-01'))
        self.assertEqual(result['current_year'], make_date('2017-01-01'))
        self.assertEqual(len(result['years']), 2)
        self.assertEqual(result['years'][0], make_date('2015-01-01'))
        self.assertEqual(result['years'][1], make_date('2017-01-01'))


class MostSeenCreatorsTestCase(TestCase):

    def test_returns_queryset(self):
        "It should return 10 items by default."
        for i in range(11):
            EventRoleFactory()

        creators = most_seen_creators()

        self.assertEqual(len(creators), 10)

    def test_num(self):
        "It should return `num` items."
        for i in range(4):
            EventRoleFactory()

        creators = most_seen_creators(num=3)

        self.assertEqual(len(creators), 3)


class MostSeenCreatorsCardTestCase(TestCase):

    def test_returns_correct_data(self):
        for i in range(2, 13):
            # It'll cut off any with only 1 reading, so:
            EventRoleFactory.create_batch(i, creator=IndividualCreatorFactory())

        data = most_seen_creators_card()

        self.assertIn('card_title', data)
        self.assertIn('score_attr', data)
        self.assertIn('object_list', data)

        self.assertEqual(data['card_title'], 'Most seen people/groups')
        self.assertEqual(data['score_attr'], 'num_events')
        self.assertEqual(len(data['object_list']), 10)


    def test_num(self):
        "It should return `num` items."
        for i in range(2, 6):
            # It'll cut off any with only 1 reading, so:
            EventRoleFactory.create_batch(i, creator=IndividualCreatorFactory())

        data = most_seen_creators_card(num=3)

        self.assertIn('object_list', data)
        self.assertEqual(len(data['object_list']), 3)

    def test_filters_by_event_kind(self):
        "It should only count events of the supplied event_kind."

        # It should include c1 and c2 as both have > 1 GigEvent:

        c1 = IndividualCreatorFactory()
        EventRoleFactory(event=GigEventFactory(), creator=c1)
        EventRoleFactory(event=GigEventFactory(), creator=c1)
        EventRoleFactory(event=GigEventFactory(), creator=c1)
        EventRoleFactory(event=CinemaEventFactory(), creator=c1)

        c2 = IndividualCreatorFactory()
        EventRoleFactory(event=GigEventFactory(), creator=c2)
        EventRoleFactory(event=GigEventFactory(), creator=c2)

        c3 = IndividualCreatorFactory()
        EventRoleFactory(event=CinemaEventFactory(), creator=c3)
        EventRoleFactory(event=CinemaEventFactory(), creator=c3)

        data = most_seen_creators_card(event_kind='gig')

        self.assertIn('object_list', data)
        self.assertEqual(len(data['object_list']), 2)
        self.assertEqual(data['object_list'][0], c1)
        self.assertEqual(data['object_list'][0].num_events, 3)
        self.assertEqual(data['object_list'][1], c2)
        self.assertEqual(data['object_list'][1].num_events, 2)
