def retira_pontuacao(frase):
    '''Dado uma Frase, Retira as pontuacoes de uma frase, substituindo todos por espaço'''
 
frase = ()

if ":" in frase:
  frase = frase.replace(":", " ")
if ";" in frase:
  frase = frase.replace(";", " ")
if "." in frase:
  frase = frase.replace(".", " ")
if "!" in frase:
  frase = frase.replace("!", " ")
if "-" in frase:
  frase = frase.replace("-", " ")
if "," in frase:
  frase = frase.replace(",", " ")
if "?" in frase:
  frase = frase.replace("?", " ")

return frase