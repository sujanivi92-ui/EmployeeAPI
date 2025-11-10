from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # ✅ Import HttpResponse

# ✅ Simple home page view
def home(request):
    return HttpResponse(
        "<h2>Welcome to the Employee Management API!</h2>"
        "<p>Use <a href='/api/employees/'>/api/employees/</a> to access the API.</p>"
    )

urlpatterns = [
    path('', home),  # 👈 Homepage route
    path('admin/', admin.site.urls),
    path('api/', include('employees.urls')),  # 👈 Your API endpoints
]
