from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    # Redirect the root URL (/) to the admin login page
    path('', RedirectView.as_view(url='/admin/')),

    # Admin interface
    path('admin/', admin.site.urls),

    # REGDORA app
    path('regdora/', include('REGDORA.urls')),
]