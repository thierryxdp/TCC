def conta_numero(numero,matriz):
    ''' funcao que ao dar o numero inteiro e a matriz de inteiro 
    contara a retornara todas as vezes que esse inteiro aparecer nela'''
    quantidade= 0
    for linha in matriz:
        quantidade = quantidade + list.count(linha,numero)
    return quantidade