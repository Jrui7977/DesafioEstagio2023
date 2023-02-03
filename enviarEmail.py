import smtplib #protocolo padrão de comunicação entre email
import email.message
from tkinter import *
from tkinter import messagebox

def enviar_email(remetente, destinatario, assunto):

    corpo_email = """
    <p>Olá, meu nome é José Rui e estou participando do PROGRAMA DE ESTÁGIO TALENT LAB ITACOATIARA (Nível Superior).</p>
    """
    msg = email.message.Message()
    msg['Subject'] = assunto
    msg['From'] = remetente
    msg['To'] = destinatario
    password = 'oxznmhczyhonhycb' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587') #dominio do email, cada tipo de protocolo tem uma configuração diferente
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    messagebox.showinfo("Sucesso","Email enviado!")

def criaJanela():
    
    #definindo os destinatários

    remetente  = 'jrui797@gmail.com'
    assunto = 'DESAFIO TALENT LAB ITACOATIARA'
    destinatario1 = 'alfredobarros@bemol.com.br'
    destinatario2 = 'juanoliveira@bemol.com.br'
    destinatario3 = 'emariellealmeida@bemol.com.br'

    janela = Tk()
    janela.geometry("300x150")
    janela.title("Escrever email")

    From = Label(janela, text = remetente)
    From.grid(column = 0, row = 0)

    Subject = Label(janela, text = "Assunto : " + assunto)
    Subject.grid(column=0, row = 1)

    toFirst = Label(janela,text = destinatario1)
    toSecond = Label(janela,text = destinatario2)
    toThird = Label(janela,text = destinatario3)

    toFirst.grid(column=0, row = 2)
    toSecond.grid(column=0, row = 3)
    toThird.grid(column=0, row = 4)

    SendFirst = Button(janela, text = 'Enviar', command= lambda:enviar_email(remetente,destinatario1,assunto))
    SendSecond = Button(janela, text = 'Enviar', command= lambda:enviar_email(remetente,destinatario2,assunto))
    SendThird = Button(janela, text = 'Enviar', command= lambda:enviar_email(remetente,destinatario3,assunto))

    SendFirst.grid(column=1,row=2)
    SendSecond.grid(column=1,row=3)
    SendThird.grid(column=1,row=4)
    
    janela.mainloop()
    

criaJanela()


