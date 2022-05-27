
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from myblog.views import home_view,create_view,detail_view,update_view,delete_view
from froala_editor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name="home"),
    path('froala_editor/',include('froala_editor.urls')),
    path('createblog/',create_view,name="create"),
    path('blogDetail/<int:pk>/',detail_view,name="detail"),
    path('blogUpdate/<int:pk>/',update_view,name="update"),
    path('delete/<int:pk>/',delete_view,name="delete"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)