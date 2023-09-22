def filtra_pares(x):
    '''Calcule e retorne uma função que receba uma tupla com 4 caracteres inteiros e retorne uma nova dupla contendo os caracteres pares da tupla original '''
    tupla = ()
    tupla1 = int(x[0])
    tupla2 = int(x[1])
    tupla3 = int(x[2])
    tupla4 = int(x[3])
    
  
    
    if tupla1%2 == 0:
        tupla = tupla + (tupla1,)
    
    if tupla2%2 == 0:
        tupla = tupla + (tupla2,)
    
    if tupla3%2 == 0:
        tupla = tupla + (tupla3,)
    
    if tupla4%2 == 0:
        tupla = tupla + (tupla4,)
        return tupla