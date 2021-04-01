from django.contrib import admin, auth
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
   ## path('login/', LoginView.as_view(template_name='polls/login.html')),
##	path('logout/', LogoutView.as_view(next_page='/polls')),
]
