# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    user_text = request.GET['text']
    total_count = len(user_text)
    work_dict = {}
    for word in user_text:
        if word not in work_dict:
            work_dict[word] = 1
        else:
            work_dict[word] += 1
    sorted_dict = sorted(work_dict.items(), key=lambda w: w[1], reverse=True)

    return render(request, 'count.html',
                  {'count': total_count, 'user_text': user_text, 'sorted_dict': sorted_dict})
