def farinha( farinha):
    'Calcula a quantidade de farinha necessária para uma receita
    int -> int'''
    return floor ( farinha / 2)
    
def ovos( ovos):
    '''Calcula a quantidade de ovos necessária para uma receita
    int -> int'''
    return floor ( ovos / 3) 
    
def leite( leite):
   '''Calcula a quantidade de leite necessária para uma receita
    int -> int'''
  	return floor ( leite / 5)

def bolos ( farinha, ovos, leite):
    '''Calcula o número de bolos que podem ser feitos com determinada
    quantidade  de xícaras de farinha de trigo, de ovos e de colheres de 
    sopa de leite
    int,int -> int'''
    return flor(farinha(farinha) + ovos(ovos) + leite(leite) / 10)