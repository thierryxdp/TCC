def uppCons(frase):
    ''' funcao retorna apenas as consoantes da frase em maiusculas. str->str'''
    i=0
    lista=[]
    while i+1<= len(frase):
        if frase[i] not in 'aeiouAEIOU':
            lista.append(frase[i])
        i+=1
    lista="".join(lista)
    return lista.upper()