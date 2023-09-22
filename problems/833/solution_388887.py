def conta_numero(numero, matriz):
    ''' funcao que dado o número inteiro e uma matriz de inteiro
    conta e retorna quantas vezes esse inteiro aparece nela'''
    
    quantidade = 0
    for linha in matriz:
        quantidade = quantidade + list.count(linha, numero)
        return quantidade