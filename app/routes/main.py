from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['POST'])
def login():
    # Aqui você pode adicionar a lógica de autenticação
    return "Login bem-sucedido!"