import os 
import win32com.client as win32 
import base64 
from datetime import datetime

def send_email(dir_print, destinatarios, cc_destinatarios):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    
    dir = f'prints/{dir_print}'
    images = os.listdir(dir)
    
    data_atual = datetime.now().strftime("%d/%m/%Y")
    assunto = f'RELATÓRIO SFM: SOLDA DIÁRIA - {data_atual}'
    titulo = f"<h1>Bom dia, segue o relatório - {data_atual}</h1>"

    # Loop em toda a pasta das imagens
    html_body = f"<html><body>{titulo}"

    for image_name in images:
        image_path = os.path.join(dir, image_name)
        if os.path.isfile(image_path):
            with open(image_path, 'rb') as f:
                image_data = f.read()
                image_base64 = base64.b64encode(image_data).decode('utf-8')
                image_html = f"<p><img src='data:image/jpeg;base64,{image_base64}'></p>"
                html_body += image_html
                
    html_body += "</body></html>"

    footer = "<p>Email enviado por automatização</p>"
    html_body += footer
    destinatario = destinatarios
    mail.To = destinatario
    mail.CC = cc_destinatarios
    mail.Subject = assunto
    mail.HTMLBody = html_body
    mail.Send()