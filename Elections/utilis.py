# Elections/utils.py
from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import Group

def user_in_group(user, group_name):
    if not user.is_authenticated:
        return False
    return user.groups.filter(name=group_name).exists() or user.is_superuser

def role_required(allowed=None, redirect_to='elections:dashboard', message=None):
    """
    Decorator: allowed can be a string or list/tuple of allowed groups.
    Example: @role_required('Admin') or @role_required(['Admin','ElectionManager'])
    """
    if isinstance(allowed, str):
        allowed_list = [allowed]
    else:
        allowed_list = allowed or []

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            for g in allowed_list:
                if user_in_group(request.user, g):
                    return view_func(request, *args, **kwargs)
            # not allowed
            if message:
                messages.error(request, message)
            else:
                messages.error(request, "You don't have permission to access that page.")
            return redirect(redirect_to)
        return _wrapped
    return decorator
