import speedtest
teste = speedtest.Speedtest()
download = teste.download()*10**-6
upload = teste.upload()*10**-6

print(f'download(mb/s): {download}')
print(f'upload(mb/s): {upload}')
