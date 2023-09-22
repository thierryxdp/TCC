def conta_numero(numero,matriz):
    '''Função que conta quantas vezes um numero inteiro 
    aparece dentro de uma matriz dado esse numero;int,list->int'''
    n=0
    for linha in matriz:
        n= n + list.count(linha,n)
    return n