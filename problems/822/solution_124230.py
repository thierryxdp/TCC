def repetidos (lista: list) -> int:
    """Função que recebe uma lista de números e retorna o números de vezes que um elemento da lista é igual ao elemento anterior."""
    numero = 0
    i = 0
    f = 1
    while i <= len(lista):
        compara = lista[i]
        compara2 = lista[f]
        if compara == compara2:
       		 numero = numero + 1
        i = i + 1
        f = f + 1
    return numero