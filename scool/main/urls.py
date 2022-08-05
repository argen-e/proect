from django.urls import path
from .views import home, home_1, home_2




urlpatterns = [

    path(' /', home),
    path('teacher/', home_1),
    path('pupil/', home_2)

]
