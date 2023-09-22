def faltante(lista):
    """Recebe uma lista com 'N-1' inteiros numerados de 1 a N 
       e retorna o número que está faltando
       parâmetro de entrada:list
       parâmetro de saída:int"""
    
    indice=1
    x=0
    while x<len(lista):
        if not (x+1 in lista):
            return x+1
        x=x+1