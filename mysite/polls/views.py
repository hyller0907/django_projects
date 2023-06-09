from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


# def index(request):
#     """
#     That is my main page
#         # urls.py
#             path('', views.index, name='index'),
#
#         # template: index.html
#             {% if latest_question_list %}
#                 <ul>
#                 {% for question in latest_question_list %}
#                     <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
#                 {% endfor %}
#                 </ul>
#             {% else %}
#                 <p>No polls are available.</p>
#             {% endif %}
#
#     When we create the list, we append the "question.id" into each href, for example:
#         <a href="/polls/3/">What is your name?</a>
#         <a href="/polls/2/">Answer to the Ultimate Question</a>
#
#         That way the user will click on that, and we can extract the "question.id" to better work with it.
#
#         # ===============
#         # Attention
#         # ===============
#         If i use this approach with the table of portfolios, I can directly render the user
#         into the comment session.
#         Maybe that is an interesting solution to get into the comments of each portfolio!
#     """
    # That you pull all the questions of my models and presented it as a list in my main page
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # print(latest_question_list)
    #
    # context = {"latest_question_list": latest_question_list}
    # return render(request, "polls/index.html", context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


def owner(request):
    """
        That is from the coursera week 2 assignment.

        Django will return an HTTP RESPONSE with the text below. An interesting detail is that we do not have any
        template associated with this view.
    """
    return HttpResponse("Hello, world. 533935c8 is the polls owner.")


# def detail(request, question_id):
#     """
#     Once you have your href connected with each of your model ids, you can use it to search for the
#     questions that matches the id informed.
#
#         # urls.py
#             path('<int:question_id>/', views.detail, name='detail'),            # ex: /polls/5/
#
#         # template: detail
#             <h1>{{ question.question_text }}</h1>
#             <ul>
#                 {% for choice in question.choice_set.all %}
#                     <li>{{ choice.choice_text }}</li>
#                 {% endfor %}
#             </ul>
#
#         # models.py
#             class Question(models.Model):
#                 question_text = models.CharField(max_length=200)
#                 pub_date = models.DateTimeField("date published")
#                 def __str__(self):
#                     return self.question_text
#
#                 def was_published_recently(self):
#                     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#     """
#     try:
#         print(f'The question id for the selection is: {question_id}')
#         question = Question.objects.get(pk=question_id)
#
#         my_choice = Choice.objects.filter(question=question)
#         print(f'The choices to this question are: {my_choice}')
#
#         context = {'question':question}
#
#     except:
#         raise Http404("This question does not exist, please try again")
#
#     return render(request, "polls/detail.html", context)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    print('Information that came in')
    print('Request:', request)
    print('Question ID:', question_id)

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
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
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))