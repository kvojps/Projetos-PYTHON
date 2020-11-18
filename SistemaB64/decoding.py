import base64

arquivo = open('textoCodificado')
arquivoRead = arquivo.read()

base_String = arquivoRead.encode('UTF-8')
decodificarBase64 = base64.b64decode(base_String)
print('Decodificado',decodificarBase64)