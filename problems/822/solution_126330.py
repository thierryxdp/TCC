def repetidos(list):
    '''Função que ao receber uma lista de números, retorna
    com o quantitativo de vezes que um elemento da lista é
    igual ao elemento anterior.
    str -> int'''   
    i=2
    nova_lista=[]
    while i<len(list):
        if list[i]==list[i-1]:
            nova_lista=nova_lista+[1]
        i=i+1
    return nova_lista