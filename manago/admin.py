from django.contrib import admin
from .models import *
# Register your models here.


class all_admin(admin.ModelAdmin):
	#myModels=['models.client_data','models.developer_data','models.admin_data']
	admin.site.register(client_data)
	admin.site.register(admin_data)
	admin.site.register(developer_data)
	admin.site.register(Attachment)

	