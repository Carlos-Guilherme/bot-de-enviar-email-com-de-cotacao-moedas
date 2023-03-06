import smtplib
import email.message
import datetime
import time
import requests

def enviar_email():  
    corpo_email = f"""
    <div style="background-color: rgb(58, 180, 89);width: 300px;padding: 20px;text-align: center;font-family: Arial, Helvetica, sans-serif;border-radius: 30px;">
        <h1>Cotação Hoje</h1>
        <p style="font-size: 25px;">BTC: {cotacao_btc} R$</p>
        <p style="font-size: 25px;">Euro: {cotacao_euro} R$</p>
        <p style="font-size: 25px;">Dolár: {cotacao_dolar} R$</p>
    </div>
    """
    msg = email.message.Message()
    msg['Subject'] = "Cotação de moedas"
    msg['From'] = 'Email que fará o envio'
    msg['To'] = 'Email que receberá'
    password = 'Senhas de App' # acesse aqui para gerar a sua: https://myaccount.google.com/u/1/security
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

# Defina o horário em que você quer que seu código execute (formato HH:MM)
horario_execucao = '7:00'

while True:
    # Obtenha a hora atual do sistema
    hora_atual = datetime.datetime.now().strftime('%H:%M')
    # Verifique se a hora atual é igual ao horário de execução
    if hora_atual == horario_execucao:
        # Se for igual, execute o seu código aqui
        
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

        requisicao_dic = requisicao.json()
        cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
        cotacao_euro = requisicao_dic["EURBRL"]["bid"]
        cotacao_btc = requisicao_dic["BTCBRL"]["bid"]
        enviar_email()
    time.sleep(60)
