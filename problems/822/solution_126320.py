def repetidos(list):
    '''Função que ao receber uma lista de números, retorna
    com o quantitativo de vezes que um elemento da lista é
    igual ao elemento anterior.
    str -> int'''   
    i=0
    n=1
    while i<len(list):
        if i<n and list[i]==list[n]:
            n=n+1
        i=i+1
    return i