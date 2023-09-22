def insere(lista_numero,n):
    """ Função que recebe um número 'n' e inclui o 'n' 
    na posição correta da lista ordem crescente.
    Entrada:lista,int
    Saída: lista """
    y = [n]
    soma = lista_numero + y
    list.sort(soma)
    return soma