from django.shortcuts import render
from .nums import generate_numbers, verify_num, validate_num


N = 4
x = generate_numbers(N)
count = 0
entry = {}


def res(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        global x
        global count
        global entry
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

        count += 1
        context = {
            'numbers': request.POST.get('numbers'),
            'flag': True,
            'msg': msg,
            'reset': reset,
            'count': count,
        }

        entry[count] = context
        return render(request, 'index.html', context)


def index_view(request):
    return render(request, 'index.html')


def view_hist(request):
    return render(request, 'history.html', entry)

