def faltante(L):
    '''Função que recebe uma lista(L) de números int;
identifica qual int está faltando no intervalo de [1,N];
retorna um int referente ao que está faltando na lista original.
list-> int'''
    L.sort()
    i = 1
    while i in L:
        i = i + 1
    return i