import smtplib

s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("email_remetente","senha_remetente")
mensagem = "python é mais que uma linguagem, é sim um estilo de vida"
s.sendmail("email_remetente","email_destinatário",mensagem)
s.quit()