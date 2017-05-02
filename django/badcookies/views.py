from django.http import HttpResponse

def hello(request):
    output = ''
    output += "Cookie header raw: {}\n".format(request.META['HTTP_COOKIE'])
    output += "Cookies: {}".format(request.COOKIES)
    return HttpResponse(output, content_type='text/plain') 
