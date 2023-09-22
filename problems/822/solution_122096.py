def repetidos(lista):
    "Recebe como entrada uma lista de numero e retorna numero de vezes de um elemento."
    i=1
    j=0
    elementos=0
    while j< len(lista)-1:
        if lista[i] == lista[j]:
            i=i+1
            j=j+1
            elementos= elementos + 1
    return elementos