def repetidos (lista: list) -> int:
    """Função que recebe uma lista de números e retorna o números de vezes que um elemento da lista é igual ao elemento anterior."""
    numero = 0
    i = 1
    while i <= len(lista):
        if lista[i:i+1] == lista [i+1:i+2]:
        	numero = numero + 1
        i = i + 1
    return numero