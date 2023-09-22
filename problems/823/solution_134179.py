def faltante(lista_numeros):
    """ Função que dada uma lista de números com N-1 inteiros
        numerados de 1 a N (sendo N o número de peças de um 
        quebra-cabeças), retorna qual numero inteiro deste 
        intervalo está faltando;
        list(int) => int"""
    i = 0 #representa os números de 1 a N 
    while i<=len(lista_numeros):
        i = i+1
        if i not in lista_numeros:
            return i