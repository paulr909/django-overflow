from django.contrib import admin
from django.urls import include, path

import qanda.urls
import user.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include(user.urls, namespace="user")),
    path("", include(qanda.urls, namespace="questions")),
]
