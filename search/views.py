from django.shortcuts import render

from django.views.generic import ListView
from products.models import Product

class SearchProductView(ListView):
    template_name = "products/list.html"
    def get_queryset(self, *args, **kargs):
        request = self.request
        return Product.objects.all()
