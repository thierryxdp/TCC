def repetidos(lista):
    """Função que ao receber uma lista de números, retorna a quantidade
    de vezes que um elemento da lista é igual ao anterior;
    list -> int"""
    i=0
    num=0
    while i < len(lista):
        if lista[i-1] == lista[i]:
            num +=1
        i+=1
    return num