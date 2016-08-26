from epflutils.decorators import cache_anonymous_user

@cache_anonymous_user(settings.CACHE_TIMEOUT)
def homepage(request):


