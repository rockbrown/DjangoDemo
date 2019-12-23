from django.contrib import admin

# Register your models here.
from .models import Posts
admin.site.register(Posts)

from .models import Mst_Post_Statuses
admin.site.register(Mst_Post_Statuses)
