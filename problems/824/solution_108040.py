def uppCons(frase):
    """recebe uma frase e retorna a mesma com suas consoantes maiúscuas
    str->str"""
    indice=0
    lista1=[]
    while indice<len(frase):
        if frase[indice] not in 'AEIOUaeiouÁÉÍÓÚáéíóú':
            lista1+=[str.upper(frase[indice])]
        if frase[indice] in 'AEIOUaeiouÁÉÍÓÚáéíóú':
            lista1+=[frase[indice]]
        indice+=1
    a=''.join(lista1)
    return a