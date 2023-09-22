def uppCons(frase):
    """recebe uma frase e retorna a mesma com suas consoantes maiúscuas
    str->str"""
    lista=frase.split()
    indice=0
    lista1=[]
    b=lista[indice]
    while indice<len(lista):
        if lista[indice] not in 'aeiouAEIOU':
            lista1+=[str.upper(b)]
        if lista[indice] in 'aeiouAEIOU':
            lista1+=[b]
        indice+=1
    a=' '.join(lista1)
    return a