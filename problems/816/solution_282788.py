def maiores(lista,n):
    """retorna outra lista com os números maiores que n"""
    list.append(lista,n)          #insere o elemento n na lista
    list.sort(lista)              #ordena os elementos da lista
    posicao = list.index(lista,n) #retorna a posição do elemento n
    del lista [:posicao+1]        #remove n e os elementos antes dele 
    return lista