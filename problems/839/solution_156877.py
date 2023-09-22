import math
    
     def carros( p , v=5) :
        ''' Função que calcula quantos veículos (v, padrão de capacidade 5) são necessários para transportar (p) pessoas. '''
    resultado = math.ceil(p/v)
    return resultado