def maiores(listaN,n):
    """ funcao que dada uma lista de numeros inteiros, retorna outra lista com um outro numero n e contenha todos os numeros da lista em ordem crescente"""
    list.append(listaN,n)   
    list.sort(listaN)
    ordem=listaN.index(n)
    return listaN[ordem+1:]