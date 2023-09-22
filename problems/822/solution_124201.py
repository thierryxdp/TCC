def repetidos(lista):
    " essa funcao recebe como entrada uma lista e retorna o numero de vezes que um elemento da lista e igual ao elemento anterior;list-> int"
    i=1
    r=[]
    while i < len(lista):
        if lista[i]==lista[i-1]:
            r.append(lista[i])
        i=i+1
    return len(r)