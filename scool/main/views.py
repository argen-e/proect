from django.shortcuts import render



from .models import (
    Teacher, Pupil
)

def home(request):
    teacher = Teacher.objects.all()
    pupil = Pupil.objects.all()

    context = {
        'teachers': teacher,
        'pupils': pupil
    }
    return render(request, 'main/home.html', context)


def home_1(request):
    teacher = Teacher.objects.all()

    context = {
        'teachers': teacher,
    }
    return render(request, 'main/teacher.html', context)



def home_2(request):
    pupil = Pupil.objects.all()

    context = {
        'pupils': pupil
    }
    return render(request, 'main/pupil.html', context)
# Create your views here.
