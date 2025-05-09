from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    """
    Endpoint que simula o envio de e-mail.

    Retorna:
        JSON com status de sucesso e mensagem simulada.
    """
    data = request.get_json()
    print("📧 Simulando envio de e-mail com os dados:")
    print(data)
    return jsonify({
        "status": "sucesso",
        "mensagem": "E-mail enviado com sucesso (simulado)"
    }), 200

if __name__ == '__main__':
    app.run(port=5000)
