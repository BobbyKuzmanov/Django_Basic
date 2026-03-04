from django.urls import path, re_path, include

from urlsAndViews.department.views import index, view_with_name, view_with_int_pk, view_with_slug, show_archive

urlpatterns = [
    path('', index),
    path('numbers/', include([
        path('<int:pk>/', view_with_int_pk),
        path('<int:pk>/<slug:slug>/', view_with_slug),
    ])),
    re_path(r'^archive/(?P<archive_year>202[0-3])/$', show_archive),
    path('<variable>/', view_with_name),

]
