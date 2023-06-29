from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from CarApp.views import categories
from CarApp.views import home
from CarApp.views import contact
from CarApp.views import tires
from CarApp.views import cart, delete_item
from django.contrib.auth import views as auth_views
from CarApp.views import upload, signup, batteries, maintenance, clothing, helmets, motoroil,payment

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('categories/', categories, name="categories"),
                  path('home/', home, name="home"),
                  path('contact/', contact, name="contact"),
                  path('Tires/', tires, name="tires"),
                  path('Batteries/', batteries, name="batteries"),
                  path('Maintenance/', maintenance, name="maintenance"),
                  path('Clothing/', clothing, name="clothing"),
                  path('Helmets/', helmets, name="helmets"),
                  path('Motor-Oil/', motoroil, name="motoroil"),
                  path('cart/', cart, name='cart'),
                  path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
                  path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
                  path('upload/', upload, name="upload"),
                  path('signup/', signup, name="signup"),
                  path('payment/', payment, name="payment")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
