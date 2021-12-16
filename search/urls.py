from django.urls import path

app_name = "search"

from products.views import (
                        ProductListView, 
                    )
urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
]