def insere(listanum,num):
    """Função que dada uma lista ordenada (crescente) de n° inteiros e um n° inteiro n, 
    inclua n na posição correta, ou seja, de tal maneira que a lista continue ordenada;
    list, int -> list"""
    list.append(listanum,num)
    list.sort(listanum)
    return listanum