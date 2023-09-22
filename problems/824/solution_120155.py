def uppCons(texto):
    cont=0
    texto_cons=''
    while cont<len(texto):
        if texto[cont]in'bcçdfghjlmnpqrstvxzBCÇDFGHJLMNPQRSTVXZ'
           texto_cons +=[texto[cont].upper()
        else:
           texto_cons +=texto_cons[cont]
           cont=cont+1
           return texto_cons