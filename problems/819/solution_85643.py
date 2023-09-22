def filtraMultiplos(ls,n):
    '''Função que filtra os múltiplos de um n dado, que recebe como entrada
uma lista de números e um número e retorna outra lista contendo todos os ele-
mentos da lista original que forem divisíveis por n.
'''
    multiplos=[]
    for x in ls:
        if x%n==0:
            list.append(multiplos,x)
    return multiplos