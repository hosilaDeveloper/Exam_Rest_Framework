from django.urls import path
from .views import ContactView, AboutView, CustomRegisterView, LoginView, LogoutView, TurPaketView, ImageView

urlpatterns = [
    path('register/', CustomRegisterView.as_view(), name='register-list'),
    path('contact/', ContactView.as_view(), name='contact-list'),
    path('about/', AboutView.as_view(), name='about-list'),
    path('login/', LoginView.as_view(), name='login-list'),
    path('logout/', LogoutView.as_view(), name='logout-list'),
    path('paket/', TurPaketView.as_view(), name='paket-list'),
    path('images/', ImageView.as_view(), name='image-list')
]
