def faltante(lista):
    '''
Funçao que dada uma lista de números inteiros, retorna
o número que está faltando no intervalo da lista dado.

list-->int
    '''
   
    falta=lista[:]
    falta.sort()
    i=0
    p_faltante=-1
    while i <len(falta):
        if falta[i]==i+1:
            i=i+1
        else:
            p_faltante=i+1
            i= len(falta) 
    if p_faltante==-1:
        p_faltante=len(falta)+1
    return p_faltante