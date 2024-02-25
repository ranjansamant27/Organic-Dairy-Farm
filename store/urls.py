from django.urls import path
from . import views
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('',views.index,name='indexpage'),
    path('login/',views.login_view,name='loginpage'),
    path('logout/',views.logout_view,name='logoutpage'),
    path('signup/',views.signup_view,name='signuppage'),
    path('productdetails/<item_id>/',views.productdetails,name='productdetailpage'),
    path('addtocart/<pid>/',views.addtocart),
    path('viewcart/',views.viewcart),
    path('catfilter/<cid>/',views.catfilter),
    path('remove/<id>/',views.removefromcart),
    path('updateqty/<id>/<qv>/',views.updateqty),
    path('clearcart/',views.clearcart),
    path('checkout/',views.checkout),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
