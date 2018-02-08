from django.conf.urls import include, static, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from spectator.core.sitemaps import CreatorSitemap
from spectator.events.sitemaps import EventSitemap, VenueSitemap, WorkSitemap
from spectator.reading.sitemaps import PublicationSitemap,\
        PublicationSeriesSitemap


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('spectator.core.urls')),

    url(r'^sitemap\.xml$',
        sitemap,
        {
            'sitemaps': {
                'publications': PublicationSitemap,
                'publicationseries': PublicationSeriesSitemap,
                'works': WorkSitemap,
                'events': EventSitemap,
                'venues': VenueSitemap,
                'creators': CreatorSitemap,
            },
        },
        name='django.contrib.sitemaps.views.sitemap'),
]


from django.conf import settings

if settings.DEBUG:

    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

    urlpatterns += \
        static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += \
        static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
