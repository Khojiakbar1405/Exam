from django.contrib import admin
from .models import (
    Construction,
    Project,
    ListProject,
    Blog,
    Contact
) 
# Qurulishlar uchun
admin.site.register(Construction)
# Bosh sahifadagi Loyixalar uchun
admin.site.register(Project)
# Loyixalar sahihasi uchun
admin.site.register(ListProject)
# Blog qisim uchun
admin.site.register(Blog)
# Bog`lanish uchun
admin.site.register(Contact)
