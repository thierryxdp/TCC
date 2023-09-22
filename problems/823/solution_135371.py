def faltante(lista):
    """Função que, dada uma lista com N-1 inteiros, numerados de 1 a N, retorna o número inteiro desse intervalo que está faltando; lista->int"""
    
    contador = 0
    
    while contador < len(lista):
        
        if lista[contador]+1 != lista[contador+1]:
            return lista[contador]
        contador = contador+1