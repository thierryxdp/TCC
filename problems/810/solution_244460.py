# A função recebe uma frase e retorna outra frase que contenha as mesmas palavras da frase de
# entrada na ordem inversa, sem letras maiúsculas e sem pontuação.
# string->string
#
def inverte(frase):    
    frase=str.lower(frase)
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.split(frase)
    list.reverse(frase)
    strfrase=" ".join(frase)
    return strfrase