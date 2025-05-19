from django.urls import path, include

urlpatterns = [
    path('web_app/', include('web_app.urls')),
]
