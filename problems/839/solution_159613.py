input
def carros(numero_de_pessoas, quantidade_de_carros):

 
    r = numero_de_pessoas %  quantidade_de_carros
    q = numero_de_pessoas // quantidade_de_carros
    
    if r > 0:
     		s = q + 1
    else:
    		s = q
       
    return s