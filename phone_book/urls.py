from django.conf.urls.static import static
from django.urls import path

from my_project import settings
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user-details'),
    path('add_user', views.AddUser.as_view(), name='add_user'),
    path('user/edit/<int:pk>', views.UpdateUser.as_view(), name='update_user'),
    path('user/delete/<int:pk>', views.DeleteUser.as_view(), name='delete_user'),
    path('search_result', views.SearchResultsView.as_view(), name='search'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
