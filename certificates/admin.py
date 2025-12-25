from django.contrib import admin
from .models import Certificate, Teacher, Course


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        'serial',
        'certificate_id',
        'last_name',
        'first_name',

        'course',
        'teacher',
        'certificate_given_date',
    )
    list_display_links = ('first_name', 'last_name', 'certificate_id', )

    search_fields = (
        'certificate_id',
        'first_name',
        'last_name',
        'father_name',
        'teacher'
    )

    list_filter = (
        'course',
        'teacher',
        'certificate_given_date',
        'created_at',
    )

    ordering = ('-created_at',)

    # 🔐 O‘zgartirib bo‘lmaydigan maydonlar
    readonly_fields = (
        'serial',
        'qr_code',
        'created_at',
    )

    # autocomplete_fields = ('course', 'teacher')

    # 📝 Formani tartibli ko‘rsatish
    # fieldsets = (
    #     ("🆔 Sertifikat ma'lumotlari", {
    #         'fields': ('serial', 'certificate_id', 'qr_code')
    #     }),
    #     ("👤 Talaba F.I.Sh", {
    #         'fields': ('last_name', 'first_name', 'father_name')
    #     }),
    #     ("📚 Ta'lim ma'lumotlari", {
    #         'fields': ('course', 'teacher')
    #     }),
    #     ("📅 Sanalar", {
    #         'fields': (
    #             'study_start_date',
    #             'study_end_date',
    #             'certificate_given_date',
    #             'created_at',
    #         )
    #     }),
    # )

    # add_fieldsets = (
    #     ("Yangi sertifikat qo‘shish", {
    #         'fields': (
    #             'certificate_id',
    #             'last_name',
    #             'first_name',
    #             'father_name',
    #             'course',
    #             'teacher',
    #             'study_start_date',
    #             'study_end_date',
    #             'certificate_given_date',
    #         )
    #     }),
    # )

    # 📌 Jadvaldan tez o‘zgartirish
    # list_editable = ('course', 'teacher')

    # 🔢 Har sahifada nechta obyekt
    list_per_page = 25



@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')
    search_fields = ('full_name',)
    ordering = ('full_name',)
    list_per_page = 20



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 20
