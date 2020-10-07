from pytube import YouTube

#Colocar link do video
yt = YouTube('')
stream = yt.streams.first()

#Você pode deixar vazio para baixar no diretório atual
#Ou pode adicionar o path
stream.download('')

print('Download finalizado')
