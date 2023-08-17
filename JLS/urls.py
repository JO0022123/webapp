from .import views
from django.urls import path
urlpatterns = [
  path('',views.home,name="home"), 
   path('je/',views.je,name="je"),  
    path('category/<str:name>',views.collectionsview,name="category"),
     path('category/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('ring/',views.ring,name="ring"), 
    path('chain/',views.chain,name="chain"), 
    path('bracelet/',views.bracelet,name="bracelet"), 
    path('necklace/',views.necklace,name="necklace"), 
    path('bangle/',views.bangle,name="bangle"), 
    path('earring/',views.earring,name="earring"), 
    path('about/',views.about,name="about"), 
     path('contact/',views.contact,name="contact"), 
     path('login/',views.login_page,name="login"),  
     path('signup/',views.signup,name="signup"),   
      path('logout',views.logout_page,name="logout"),  
       path('cart',views.cart_page,name="cart"),
        path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),  
      path('addtocart',views.add_to_cart,name="addtocart"),
]
