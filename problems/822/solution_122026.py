def repetidos(lista:list)->int:
    """Dada uma lista, calcula e retorna o número de vezes que houve um valor igual ao anterior."""
    repeticoes=[]
    posicao=0
    while posicao<len(lista):
        if lista[posicao]==lista[proximo-1]:
            repeticao.append(1)
            posicao=posicao+1
        return repeticoes