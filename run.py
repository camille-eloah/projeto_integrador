from app import create_app

# Cria a instância da aplicação Flask
app = create_app()

if __name__ == '__main__':
    # Roda o servidor localmente, permitindo a depuração e recarregamento automático durante o desenvolvimento
    app.run(debug=True)
