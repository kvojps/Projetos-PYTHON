from googletrans import Translator

texto = "Divers_tech é uma ótima página para aprender sobre python."
tradutor = Translator()

#detector de linguagem
idioma = tradutor.detect(texto)
print('Idioma: ', idioma)

traducao = tradutor.translate(texto)
print(traducao.text)
