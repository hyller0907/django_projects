from django.http import HttpResponse


def myview(request):
    # print(f'Seus cookies sao: {request.COOKIES}')

    # Checking the client
    trigger_check = request.COOKIES.get('num_visits', 0)
    # print(f'Seu trigger e: {trigger_check}')

    # Se o cliente esta visitando o nosso site pela primeira vez e nao possui cookie
    if trigger_check is None:
        # Initiating the cookie
        resp = HttpResponse('view count=' + str(trigger_check))
        resp.set_cookie('num_visits', 1)

    # Neste caso o cliente ja possui cookie e iremos aumentar o parametro 'num_visits' da session
    else:
        # Once the client has the cookie you can extract information from the session directly
        num_visits = request.session.get('num_visits', 0) + 1
        request.session['num_visits'] = num_visits
        if num_visits > 4: del (request.session['num_visits'])
        resp = HttpResponse('view count=' + str(num_visits))

    # The assignment ask to add anothe cookie
    resp.set_cookie('dj4e_cookie', 'e66292f4', max_age=1000)
    return resp
