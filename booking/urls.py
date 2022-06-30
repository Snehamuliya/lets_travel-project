# booking urls.py
from django.contrib import admin
from django.urls import path
from .views import index, signup, user_data, login, logout, holiday, book, profile, feedback, member, little_break
from .views import karnatak1, kerla, kerla2, kerla3, goa2, goa1, andman1, andman2, cor_trip, useracc_upd, family_trip
from .views import receipt, u_activity, payment, a_login, ahome, user_feedback, user_profile, user_booking
urlpatterns = [
    path('', index),
    path('sign', signup),
    path('user', user_data, name='u_data'),
    path('log', login, name='log'),
    path('alog', a_login, name='adlog'),
    path('u_logout', logout),
    path('pack', holiday),
    path('booking', book, name='book'),
    path('profile', profile, name='u_profile'),
    path('u_feedback', feedback),
    path('t_member', member, name='f_member'),
    path('kerla1', kerla),
    path('kerla2', kerla2),
    path('kerla3', kerla3),
    path('goa2', goa2),
    path('goa1', goa1),
    path('karnatak1', karnatak1),
    path('andman1', andman1),
    path('andman2', andman2),
    path('corporate', cor_trip),
    path('uaccupd', useracc_upd),
    path('family', family_trip),
    path('break', little_break),
    path('binfo', receipt, name='receipt'),
    path('activity', u_activity , name = "act"),
    path('pay', payment, name='checkout'),
    path('a_home', ahome),
    path('a_feed', user_feedback, name='feed'),
    path('a_user', user_profile, name='user'),
    path('a_book', user_booking, name='book'),
]


# https://www.xnxx3.com/video-n0u0l93/nude_girl_fucked#show-related