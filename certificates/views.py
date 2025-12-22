from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Certificate
from .forms import CertificateForm

def certificate_list(request):
    q = request.GET.get('q', '')
    certificates = Certificate.objects.filter(first_name__icontains=q)
    return render(request, 'certificates/list.html', {'certificates': certificates})

# @login_required
# @user_passes_test(lambda u: u.is_staff)
# def certificate_create(request):
#     form = CertificateForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('certificate_list')
#     return render(request, 'certificates/create.html', {'form': form})



from .utils import generate_qr

@login_required
@user_passes_test(lambda u: u.is_staff)
def certificate_create(request):
    form = CertificateForm(request.POST or None)
    if form.is_valid():
        cert = form.save(commit=False)
        cert.save()

        qr_path = generate_qr(cert.uuid)
        cert.qr_code = qr_path
        cert.save()

        return redirect('certificate_list')

    return render(request, 'certificates/create.html', {'form': form})



from django.shortcuts import get_object_or_404

def certificate_verify(request, uuid):
    cert = get_object_or_404(Certificate, uuid=uuid)
    return render(request, 'certificates/verify.html', {'cert': cert})



def home_page(request):
    context = {}
    return render(request, 'home.html', context)

