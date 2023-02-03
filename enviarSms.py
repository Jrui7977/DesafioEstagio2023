from twilio.rest import Client #importando uma biblioteca para enviar a mensagem


SID = 'AC69b9e2574bdd9dce58fb1697678ca2f9' #codigo unico de autenticação para enviar

Auth_token = '9db763b6a73ffffef0aec757ff8c18d5' #token de mensagem

de = '+18055902953' #telefone pessoal na conta da twillio

primeiroNumero = '+5597991388065'
segundoNumero = '+5592988192972'
terceiroNumero = '+5592993290162'

conteudo = 'Olá, meu nome  é José Rui e estou participando do PROGRAMA DE ESTÁGIO TALENT LAB ITACOATIARA (Nível Superior)'


def enviaMsg(Sid, token, remetente,destinatario, corpo): #definindo uma função para enviar a mensagem
    cl = Client(Sid,token)
    cl.messages.create(body = corpo , from_ = remetente, to = destinatario)

enviaMsg(SID,Auth_token,de,primeiroNumero, conteudo)
enviaMsg(SID,Auth_token,de,segundoNumero, conteudo)
enviaMsg(SID,Auth_token,de,terceiroNumero, conteudo)


