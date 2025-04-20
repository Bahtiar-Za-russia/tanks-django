from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from .models import TestUser
from django.shortcuts import get_object_or_404,render
from django.views.decorators.csrf import csrf_exempt

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html')


def results(request, question_id):
    response = "Ты смотришь на результаты вопроса %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Ты голосуешь за вопрос %s." % question_id)

@csrf_exempt
def registr(request):
    try:
        email = request.POST['email']
        password = request.POST['pass']
        user = TestUser(email=email, password=password)
        user.save()
    except:
        pass


    list_users = TestUser.objects.all()
    context = {'users': list_users}
    return render(request, 'polls/register.html', context)

def onas(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/onas.html')

def sponsor(request):
    return render(request, 'polls/sponsor.html')

def Seller(request):
    return render(request, 'polls/Seller.html')

def ss(request):
    return render(request, 'polls/ss.html')

def register(request):
    return render(request, 'polls/register.html')

def voity(request):
    return render(request, 'polls/voity.html')


