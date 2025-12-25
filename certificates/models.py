import qrcode
from io import BytesIO

from django.core.files import File
from django.db import models
from django.conf import settings

class Teacher(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="Ustoz F.I.Sh")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Ustoz"
        verbose_name_plural = "Ustozlar"

class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name="Yo‘nalish nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Yo‘nalish"
        verbose_name_plural = "Yo‘nalishlar"

class Certificate(models.Model):
    serial = models.AutoField(primary_key=True)

    certificate_id = models.CharField(
        max_length=512,
        unique=True,
        verbose_name="Sertifikat ID",
        help_text="Masalan: CERT-2025-001"
    )

    first_name = models.CharField(max_length=100, verbose_name="Ismi")
    last_name = models.CharField(max_length=100, verbose_name="Familiyasi")
    father_name = models.CharField(max_length=100, verbose_name="Otasining ismi")

    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        verbose_name="Bitirgan yo‘nalishi"
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.PROTECT,
        verbose_name="Ustoz"
    )

    study_start_date = models.DateField(verbose_name="O‘qishni boshlagan sana")
    study_end_date = models.DateField(verbose_name="O‘qishni tugatgan sana")
    certificate_given_date = models.DateField(verbose_name="Sertifikat berilgan sana")

    qr_code = models.ImageField(
        upload_to='qr/',
        blank=True,
        null=True,
        verbose_name="QR kod"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.certificate_id:
            raise ValueError("Sertifikat ID majburiy!")

        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new and not self.qr_code:
            verify_url = f"{settings.SITE_URL}/certificates/verify/{self.certificate_id}/"

            qr = qrcode.make(verify_url)
            buffer = BytesIO()
            qr.save(buffer, format='PNG')

            self.qr_code.save(
                f"certificate_{self.certificate_id}.png",
                File(buffer),
                save=False
            )

            super().save(update_fields=['qr_code'])

    def __str__(self):
        return f"{self.certificate_id} — {self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Sertifikat"
        verbose_name_plural = "Sertifikatlar"
