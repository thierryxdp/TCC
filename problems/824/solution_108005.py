def uppCons(frase):
    """recebe uma frase e retorna a mesma com suas consoantes maiúscuas
    str->str"""
    lista=frase.split()
    indice=0
    lista1=[]
    while indice<len(lista):
        if lista[indice] in 'aeiouAEIOU':
            lista1+=[lista[indice]]
        else:
            lista1+=[str.upper(lista[indice])]
        indice+=1
    a=' '.join(lista1)
    return a