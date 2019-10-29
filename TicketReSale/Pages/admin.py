from django.contrib import admin
from  .models import event

admin.site.site_header = "TeX"
admin.site.site_title = "TeX admin area"
admin.site.site_index_title = "TeX admin"

admin.site.register(event)
