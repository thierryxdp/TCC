def faltante(lista):
    """Essa função retorna o numero inteiro referente a
    peça que está faltando, dado uma lista.
    lista->int"""
    
    i=1
    list.sort(lista)
    
    #valores para comparar numeros de duas posicoes
    p1=0
    p2=0
    #verifica se o 1 esta faltando
    if lista[0] == 2:
        return 1
    #verifica qual esta faltando
    while i < len(lista):
        
        p1=lista[i]
        p2=lista[i-1]
        
        if (p2+1) != p1:
            return i+1
        i+=1
    #retorna se o ultimo estiver faltando
    return len(lista)+1