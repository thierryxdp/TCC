import re
def espaco(frase):
    #Retorna a frase onde todos os caracteres de pontução
    a= re.sub('[-,:;.!?]', ' ', frase)
    return a