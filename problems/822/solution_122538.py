def repetidos(lista):
    """Dada uma lista numérica retorna o número de vezes que um dado elemento da lista
       é numéricamente igual do que o seu sequêncial.
       list -> list"""
    
    repetidos = ()
    contador = 0
    
    while contador < len(lista):
        if lista[contador] == lista[contador+1]:
            repetidos = repetidos + (1,)
            contador = contador + 1
            return len(repetidos)