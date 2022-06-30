from django.shortcuts import render, redirect
from .nums import generate_numbers, verify_num, validate_num


N = 4
x = generate_numbers(N)


def res(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        global x
        n1 = request.POST.get('numbers')
        print(n1)
        print(type(n1))
        n2 = n1.split()
        print(x)
        print(n2)
        msg = ''
        reset = False
        if verify_num(n2):
            msg = validate_num(x, n2)
        if 'You Win!!' in msg:
            reset = True
        if reset:
            x = generate_numbers(N)


        context = {
            'numbers': request.POST.get('numbers'),
            'flag': True,
            'msg': msg,
            'reset': reset,
        }
        return render(request, 'index.html', context)


def index_view(request):
    return render(request, 'index.html')
