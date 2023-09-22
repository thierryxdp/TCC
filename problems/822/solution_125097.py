def repetidos(lista):
    """Dada uma lista de números, a função retorna a quantidade
    de vezes que um elemento da lista é igual ao elemento anterior
    à ele.
    	Exemplo: [1,2,3,3,4,4,1]. A função vai retornar 2.
        A lista deve ser escrita entre colchetes[];
        list --> int"""
    i=0
    qtd_repetidos = 0
    while i < (len(lista)):
        if lista[i] == lista[i-1]:
            qtd_repetidos = qtd_repetidos + 1
        else:
            qtd_repetidos = qtd_repetidos + 0
        i = i + 1
    return qtd_repetidos