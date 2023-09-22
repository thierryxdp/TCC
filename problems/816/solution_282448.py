def insere(lista_numero,n):
    '''dada uma lista de numeros em ordem crescente e dado
    um numero inteiro n, é retornado a lista de forma 
    crescente com o termo n em seu devido lugar'''
    x=lista_numero
    list.append(x,n)
    list.sort(x)
    return x

def maiores(lista_numero,n):
    x=insere(lista_numero,n)
    posicaoDeN=list.index(x,n)
    return x[posicaoDeN+1:]