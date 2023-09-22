def carros(amigos,lugar=5):
   
    '''
    Funçaõ que dado o número de pessoas, retorna a 
    quantidade de carros
    int,int=>int
    '''
     carros=math.ceil(amigos/lugar)
    
    return carros