def faltante(L):
    '''função que retorna a peca faltante de um quebra cabeça dados uma lista n-1
lis->int'''
    pecafaltante = 0
    while pecafaltante< len(L):
        pecafaltante= max(L)+1
    return pecafaltante