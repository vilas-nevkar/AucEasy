def is_logged_in(request):
    session = request.session
    if 'admin_username' in session:
        return True
    return False
