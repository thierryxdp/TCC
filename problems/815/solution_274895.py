def insere(lista_numero,n):
    """ Função que recebe um número 'n' e inclui o 'n' 
    na posição correta da lista ordem crescente.
    Entrada:list, int
    Saída: list """
    ordem = lista_numero + [n]
    list.sort(ordem)
    return ordem