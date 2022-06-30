from django.contrib import admin
from django.urls import path,include
# mongodemo urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls'))
]


