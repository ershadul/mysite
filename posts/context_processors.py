def host(request):
    
    return { 'host': request.get_host() }