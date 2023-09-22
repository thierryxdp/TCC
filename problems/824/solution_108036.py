def uppCons(frase):
    """recebe uma frase e retorna a mesma com suas consoantes maiúscuas
    str->str"""
    lista=frase.split()
    indice=0
    lista1=[]
    while indice<len(lista):
        if frase[indice] not in 'aeiou':
            lista1+=[str.upper(frase[indice])]
        if frase[indice] in 'aeiou':
            lista1+=[frase[indice]]
        indice+=1
    a=' '.join(lista1)
    return a