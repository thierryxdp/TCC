def repetidos (lista: list) -> int:
    """Função que recebe uma lista de números e retorna o números de vezes que um elemento da lista é igual ao elemento anterior."""
    numero = 0
    i = 0
    while lista[i] == lista [i+1]:
        numero = numero + 1
        i = i + 1
    return numero