from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Poll


# Create your views here.
def home(request):
    polls = Poll.objects.all().order_by('-pk')
    # print(polls)
    context = {
        'polls': polls
    }

    return render(request, 'poll/home.html', context)


def create(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        poll_obj = Poll(question=question, option_one=option1, option_two=option2, option_three=option3)
        poll_obj.save()
        messages.success(request, "successfully added")
        return redirect('/')
    return render(request, 'poll/create.html')


def result(request, pollId):
    poll = Poll.objects.get(id=pollId)
    total = poll.option_one_count + poll.option_two_count + poll.option_three_count
    perc1 = round((poll.option_one_count / total) * 100,2)
    perc2 = round((poll.option_two_count / total) * 100,2)
    perc3 = round((poll.option_three_count / total) * 100,2)
    context = {
        'poll': poll,
        'perc1':perc1,
        'perc2': perc2,
        'perc3': perc3,
    }

    return render(request, 'poll/result.html', context)


def vote(request, pollId):
    poll = Poll.objects.get(id=pollId)

    if request.method == 'POST':
        selected_option = request.POST.get('option')
        print(selected_option)
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form option')

        poll.save()

        return redirect('result', pollId)

    context = {
        'poll': poll
    }
    return render(request, 'poll/vote.html', context)
