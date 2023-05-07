from django.urls import path

from connections.views import Ping

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('ping/', Ping.as_view(), name="ping pong"),
]
