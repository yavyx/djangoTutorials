from django.http import HttpResponse, Http404, HttpResponseRedirect

# from django.template import loader # Used for commented code

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]  # Look for five last questions
#    template = loader.get_template('polls/index.html')  #
#    context = {
#        'latest_question_list': latest_question_list,  # Dictionary that maps the template
#                                                       # variable names to Python objects
#    }
#    return HttpResponse(template.render(context, request))  # load template (no path specified,
#                                                            # Django looks automatically in the templates folder)

# Because the above code is very common (load a template, fill a context and return an HttpResponse)
# the render() shortcut does that for us

# def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'polls/index.html', context)


# Django includes a generic index view because this is very common, see below:
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list' # specify context variables

    def get_queryset(self):
        """Return the last five published questions (not including those set to be published in the future)."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()  # return queryset containing questions whose pub_date is <= timezone.now()
        ).order_by('-pub_date')[:5]


# def detail (request, question_id):
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, 'polls/detail.html', {'question': question})

# Because the above code is very common (get an object and raise 404 if it doesn't exist)
# the get_object_or_404() shortcut does that for us

# def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question': question})

# Django includes a generic detail view because this is very common, see below:
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


#  def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question': question})

# Django includes a generic detail view because this is very common, see below:
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])  # a dictionary-like object that  lets you
#                                                                             # access submitted data by key name.
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form,
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))  # helps avoid having to hardcode a
    #                                                                           # URL in the view function
