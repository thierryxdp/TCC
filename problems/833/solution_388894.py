def conta_numero(matriz,n):
    '''Retorna quantas vezes um numero inteiro (n) aparece em uma matriz;
    list,int->int'''
    
    qtd = 0
    for linha in matriz:
        qtd += list.count(linha,n)
    return qtd