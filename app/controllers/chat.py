from flask import Blueprint, render_template, request, jsonify, session

chat_bp = Blueprint('chat', __name__, url_prefix='/chat')

@chat_bp.route('/')
def chat():
    return render_template('/chat/chat.html')

@chat_bp.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'Mensagem não pode estar vazia'}), 400

    ai_response = f"Você disse: {user_message}"  # Apenas na prototipagem!

    return jsonify({
        'user_message': user_message,
        'ai_response': ai_response
    })

