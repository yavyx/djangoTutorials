from django.http import HttpResponse, Http404

#from django.template import loader

from django.shortcuts import render, get_object_or_404

from .models import Question

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]  # Look for five last questions
#    template = loader.get_template('polls/index.html')  #
#    context = {
#        'latest_question_list': latest_question_list,  # Dictionary that maps the template variable names to Python objects
#    }
#    return HttpResponse(template.render(context, request))  # load template (no path specified, Django looks automatically in the templates folder)

# Because the above code is very common (load a template, fill a context and return an HttpResponse) the render() shortcut does that for us

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

#def detail (request, question_id):
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, 'polls/detail.html', {'question': question})

# Because the above code is very common (get an object and raise 404 if it doesn't exist) the get_object_or_404() shortcut does that for us

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)