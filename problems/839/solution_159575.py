#input 
#def carros(pessoas, capacidade=5):
#    '''calcular a quantidade de carros 
#     para realização de uma determinada viagem
#     tendo em vista o numero de pessoas para cada veículo 
#     que deve ser de no minimo cinco por 
#     carros float, float ->float '''
#    return 12*5/20

def carros(numero_de_pessoas, quantidade_de_carros):
    
    if quantidade_de_carros == [] :
       	quantidade_de_carros = 5
        
    else:
        
    	r = numero_de_pessoas %  quantidade_de_carros
    	q = numero_de_pessoas // quantidade_de_carros
    
    	if r > 0:
        	s = q + 1
    	else:
        	s = q
    
    
    return s