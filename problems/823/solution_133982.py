def faltante(lista):
    i = 0
    while i < len(lista):
   
        if lista != sorted(lista):
            listacerta = lista + [len(lista)+1]
            return sorted(listacerta)
    i = i + 1