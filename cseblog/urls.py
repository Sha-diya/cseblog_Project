

from django.contrib import admin,include
from django.urls import path
from blog.views import home, post_list,post_details

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include('blog.urls'))
    
    # path("", home),
    # path("posts/", post_list),
    # path("post_details/<int:post_id>/", post_details)
]
