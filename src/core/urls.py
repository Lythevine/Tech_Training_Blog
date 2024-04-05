from django.urls import path
from .views import HomeView, BlogView

# Create your urls here.

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogView.as_view(), name='blog'),
]