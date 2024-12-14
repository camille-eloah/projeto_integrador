from flask import Blueprint, render_template, request

auth_bp = Blueprint('auth', __name__, template_folder='../templates/auth', url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    return redirect('/')
