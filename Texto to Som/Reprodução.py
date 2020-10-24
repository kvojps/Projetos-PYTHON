import pyttsx3
#iniciando o módulo
Texto = pyttsx3.init()

# .say() é usada para reproduzir em forma de som o texto mencionado.
Texto.say("Qualquer coisa")

# Processa e roda o programa
Texto.runAndWait()
