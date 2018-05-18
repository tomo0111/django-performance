from django.conf.urls import url

from api import hello_view
from api import item_view

urlpatterns = [
    url('hello', hello_view.HelloView.as_view(), name='hello'),
    url('items', item_view.ItemView.as_view(), name='items'),
]
