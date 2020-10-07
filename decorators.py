from functools import wraps
from flask import g, request, redirect, url_for, session
from flask_session import Session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session["user"] is None:
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

def logged_in(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session["user"] is not None:
            return redirect(url_for('returns'))
        return f(*args, **kwargs)
    return decorated_function
