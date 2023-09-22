#input 
#def carros(pessoas, capacidade=5):
#    '''calcular a quantidade de carros 
#     para realização de uma determinada viagem
#     tendo em vista o numero de pessoas para cada veículo 
#     que deve ser de no minimo cinco por 
#     carros float, float ->float '''
#    return 12*5/20

def carros(numero_de_pessoas, quantidade_de_carros):
    
    a = [quantidade_de_carros]
    c = len(a)
    
    if c == 0:
        
    	r = numero_de_pessoas %  quantidade_de_carros
    	q = numero_de_pessoas // quantidade_de_carros
    
    	if r > 0:
       		s = q + 1
    	else:
       		s = q
    
    
    else:
        x = int(5)
        
        r = numero_de_pessoas %  x
    	q = numero_de_pessoas // x
    
    	if r > 0:
       		s = q + 1
    	else:
       		s = q
    
    return s