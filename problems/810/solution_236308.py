# Dada a string frase, esta função retorna uma outra string contendo as mesmas
# palavras de frase, porém em ordem inversa, sem letras maiúsculas e sem 
# pontução.
# str -> str

def inverte(frase):
    frase = frase.replace('-','')
    frase = frase.replace(',','')
    frase = frase.replace(':','')
    frase = frase.replace(';','')
    frase = frase.replace('.','')
    frase = frase.replace('!','')
    frase = frase.replace('?','')
    frase = frase.rstrip()
    frase = frase.lower()
    frase = str.split(frase,' ')
    frase = frase[len(frase)::-1]
    frase = str.join(' ',frase)
    return frase