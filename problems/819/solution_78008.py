def filtraMultiplos(lista,n):
    """Função que dada uma lista de números e um 
       número inteiro, retorna outra lista contendo
       todos os elementos da lista orginal que forem
       divisíveis por n.
       list,int->list"""
    multiplos = []
    i = 0
    while i<len(lista):
        if lista[i] % n != 0:
            list.append(multiplos,n)
        i += i + 1
         
    return multiplos