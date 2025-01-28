from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, Application
from .forms import ApplicationForm

# Список вакансий
def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'rekry/job_list.html', {'jobs': jobs})

# Детали вакансии и форма для подачи заявки
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return redirect('job_success')
    else:
        form = ApplicationForm()

    return render(request, 'rekry/job_detail.html', {'job': job, 'form': form})

# Страница подтверждения успешной подачи заявки
def job_success(request):
    return render(request, 'rekry/job_success.html')

