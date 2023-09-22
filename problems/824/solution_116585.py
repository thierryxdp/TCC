def uppCons(frase:str):
    i=0
    #String auxiliar para não perder a original.
    aux=''
    #Verifica se I é menor que a frase
    while i<len(frase):
        #verifica os caracteres da frase
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            aux += frase[i].upper()
        else:
            aux+=frase[i]
        i+=1
    return aux