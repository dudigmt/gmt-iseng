def user_groups(request):
    if request.user.is_authenticated:
        return {
            'groups': request.user.groups.all()
        }
    return {}