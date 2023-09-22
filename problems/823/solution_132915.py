def faltante(L):
    '''Função que recebe uma lista(L) de números int;
identifica qual int está faltando no intervalo de [1,N];
retorna um int referente ao que está faltando na lista original.
list-> int'''
    i = 0
    while i in range(len(L)):
        if i + 1 != L[i]:
            i = i + 1
    return len(L) + 1