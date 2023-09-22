def repetidos(lista):
    """Dada uma lista numérica retorna o número de vezes que um dado elemento da lista
       é numéricamente igual do que o seu sequêncial.
       list -> list"""
    
    contador = 0
    posicao = 0
    resultado = ()
    
    while contador < len(lista)-1:
        if lista[contador] == lista[contador+1]:
            resultado = resultado + (1,)
            contador += 1
    return len(resultado)