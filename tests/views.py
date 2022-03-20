from contextlib import nullcontext
from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Category, Question,Choice,Title,Result
from django.template import loader
from django.urls import reverse

# Create your views here.


#get questions and display
def landing(request):
    return render(request,'tests/landing.html')

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else '1'

    title_list=Title.objects.filter(category=q)
    category_list=Category.objects.all()
    context={'title_list':title_list,'category_list':category_list}
    return render(request,'tests/home.html',context)    

def index(request,pk):
    title=Title.objects.get(id=pk)
    question_list = title.question_set.all()
    
    if request.method=='POST':
        total_points=0
        result=''
        print(question_list.count())
        for question in question_list:
            try:
                selected_choice = question.choice_set.get(id=request.POST['choice_'+str(question.id)])
            except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
                return render(request, 'tests/index.html', {
                    'title': title,'question_list':question_list,
                    'error_message': "Please make choices",
                })
            else:
                total_points+=selected_choice.points    
        for point in title.result_set.all():
             if point.min_point<= total_points <=point.max_point:
                 result=point
                 break
        context={'result':result}
        return render(request,'tests/results.html',context)
        
    context ={'question_list':question_list,'title':title,}
    return render(request,'tests/index.html',context)    


        
    

def results(request,pk):
    question = get_object_or_404(Question,id=pk)
    print('result',question.id)
    context = {'question':question}
    return render(request,'polls/results.html',context)

