from django.urls import path
from cookie_sessions.controllers.web_cookie_session_ctrl import CookieSessionView

urlpatterns = [
    path('start', CookieSessionView.start_session, name='start_session'),
]