from django.urls import path
from .views import LinklistCreateView, LinkDetailView

urlpatterns = [
    path('links/', LinklistCreateView.as_view(), name='link-list-create'),
    path('links/<int:pk>/', LinkDetailView.as_view(), name='link-detail')
]