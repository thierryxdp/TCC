def repetidos(lista):
    """dada uma lista de entrada
    retorna quantas vezes os elementos
    da lista são iguais a seus antecessores
    list-->int"""
    count=1
    iguais=0
    while count<len(lista):
        if lista[count]==lista[count-1]:
            iguais=iguais+1
        count=count+1
    return iguais