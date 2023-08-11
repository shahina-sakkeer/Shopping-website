from django.urls import path
from .  import views
app_name="shop"


urlpatterns = [
    path("",views.allProdCat,name="alllist"),
    path("<slug:cat_slug>/",views.allProdCat,name="prod_by_cat"),
    path("<slug:c_slug>/<slug:product_slug>/",views.prodDetail,name="prodCatDetail")
]
