def insere(lista_numero,n):
    """Função que dada uma lista em ordem crescente de números inteiros e um número inteiro n, retorna a mesma lista com n na posição correta;list,int->list"""
    l1=list.append(lista_numero,n)
    l2=list.sort(l1)
    return l2