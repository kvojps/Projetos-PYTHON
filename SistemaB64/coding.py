import base64

arquivo = open("textoDecodificado")
arquivoRead = arquivo.read()

base_String = arquivoRead.encode('utf-8')
codificarBase64 = base64.b64encode(base_String)
print('Codificado: ',codificarBase64)

