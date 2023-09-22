""" Os ingredientes necessarios para fazer um bolo são 2 xicaras de farinha de trigo, 3 ovos e 5 colheres de sopa de leite """

def bolos(A   ## Numero de xicaras de farinha de trigo
          ,B  ## Numero de ovos
          ,C  ## Numero de colheres de sopa de leite
         ):
    
    trigo = min(A/2)
    ovo = min(B/3)
    leite = min(C/5)
    
    
    
    return min(trigo+ovo+leite)