def conta_frase(texto):
texto = texto.replace('!', '.')
texto = texto.replace('?', '.')
texto =  texto.replace('...', '.')
return texto.count('.')