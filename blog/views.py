from django.shortcuts import render


def post_list(request):
    """takes request and returns render for blog/post_list.html"""

    return render(request, 'blog/post_list.html', {})
