input
def carros(pessoas, capacidade):
 #
 
    r = pessoas %  capacidade
    q = pessoas // capacidade
    
    if r > 0:
     		s = q + 1
    else:
    		s = q
       
    return s