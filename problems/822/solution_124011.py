def repetidos (lista:list) ->int:
    """Função que recebe como entrada uma lsita de números e retorna o número de vezes que um
    elemento da lista é igual ao anterior."""
    numero = 0
    indiceinicial = 0
    indicefinal = 1
    while indicefinal <= len(lista):
        if lista[indiceinicial] == lista[indicefinal]:
            numero = numero + 1
        indiceinicial = indiceinicial + 1
        indicefinal = indicefinal + 1
    return numero