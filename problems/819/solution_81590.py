def filtraMultiplos (lista,n):
    '''Dada uma lista, filtre os múltiplos de um número n
    e retorne uma nova lista contendo os elementos da 
    original que forem diviíveis por n;
    list, int -> list'''
    i = 0
    multiplos = []
    while i<len(lista):
        if lista [i]%n == 0:
            list.append (multiplos, lista[i])
              i = i + 1
   	        return multiplos