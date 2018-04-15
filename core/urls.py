from django.conf.urls import url
from api import item_view

urlpatterns = [
    url('items', item_view.ItemView.as_view(), name='items'),
]
