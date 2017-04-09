from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        regex=r"^$",
        view=views.EventsHomeView.as_view(),
        name='events_home'
    ),

    # CONCERTS

    url(
        regex=r"^concerts/$",
        view=views.ConcertListView.as_view(),
        name='concert_list',
    ),
    url(
        regex=r"^concerts/visits/$",
        view=views.ConcertEventListView.as_view(),
        name='concert_visits',
    ),
    url(
        regex=r"^concerts/(?P<pk>\d+)/$",
        view=views.ConcertDetailView.as_view(),
        name='concert_detail'
    ),

    # MOVIES

    url(
        regex=r"^movies/$",
        view=views.MovieListView.as_view(),
        name='movie_list',
    ),
    url(
        regex=r"^movies/visits/$",
        view=views.MovieEventListView.as_view(),
        name='movie_visits',
    ),
    url(
        regex=r"^movies/(?P<pk>\d+)/$",
        view=views.MovieDetailView.as_view(),
        name='movie_detail'
    ),

    # PLAYS

    url(
        regex=r"^plays/$",
        view=views.PlayListView.as_view(),
        name='play_list',
    ),
    url(
        regex=r"^plays/visits/$",
        view=views.PlayProductionEventListView.as_view(),
        name='play_visits',
    ),
    url(
        regex=r"^plays/(?P<pk>\d+)/$",
        view=views.PlayDetailView.as_view(),
        name='play_detail'
    ),

    # MISCEVENTS

    url(
        regex=r"^misc/$",
        view=views.MiscEventListView.as_view(),
        name='miscevent_list',
    ),
    url(
        regex=r"^misc/visits/$",
        view=views.MiscEventVisitListView.as_view(),
        name='miscevent_visits',
    ),
    url(
        regex=r"^misc/(?P<pk>\d+)/$",
        view=views.MiscEventDetailView.as_view(),
        name='miscevent_detail'
    ),

    # VENUES

    url(
        regex=r"^venues/$",
        view=views.VenueListView.as_view(),
        name='venue_list',
    ),
    url(
        regex=r"^venues/(?P<pk>\d+)/$",
        view=views.VenueDetailView.as_view(),
        name='venue_detail'
    ),

    # OTHER

    url(
        regex=r"^(?P<year>[0-9]{4})/$",
        view=views.EventYearArchiveView.as_view(),
        name='event_year_archive'
    ),
]

