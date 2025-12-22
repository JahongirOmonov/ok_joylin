from django.contrib import admin
from .models import Certificate, Teacher, Course

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    readonly_fields = ('qr_code',)
    list_display = ('serial', 'first_name', 'last_name', 'course')


admin.site.register(Teacher)
admin.site.register(Course)
