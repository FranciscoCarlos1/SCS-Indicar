# Backend (Python - Flask)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from flask import app, jsonify, request

@app.route("/processar-indicacao", methods=["POST"])
def processar_indicacao():
    try:
        data = request.form
        nome = data.get("nome")
        email = data.get("email")
        telefone = data.get("telefone")
        nome_indicado = data.get("nome_indicado")
        email_indicado = data.get("email_indicado")
        empresa_indicada = data.get("empresa_indicada")
        telefone_indicado = data.get("telefone_indicado")

        # Dados para envio de e-mail
        sender_email = "suportcentersistemas.scs@gmail.com"
        sender_password = "sua_senha"
        recipient_email = "suportcentersistemas.scs@gmail.com"

        subject = "Nova Indicação Recebida"
        body = f"""
        Nome: {nome}
        E-mail: {email}
        Telefone: {telefone}

        Nome da Pessoa Indicada: {nome_indicado}
        E-mail da Pessoa Indicada: {email_indicado}
        Empresa Indicada: {empresa_indicada}
        Telefone da Pessoa Indicada: {telefone_indicado}
        """

        # Configuração do servidor de e-mail
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

        return jsonify({"message": "Indicação enviada com sucesso!"}), 200
    except Exception as e:
        print("Erro ao processar a indicação:", e)
        return jsonify({"error": "Erro ao processar sua solicitação."}), 500


