def repetidos(lista: list[int]) -> int:
    """Função que, dada uma lista de números, retorna a quantidade
    de vezes que um elemento da lista é igual ao elemento anterior."""

    contador = 0
    
    for i in range(1,len(lista)):
    	if lista[i] == lista[i-1]:
            contador = contador+1

    return contador