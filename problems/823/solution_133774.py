def faltante(lista_L):
    '''Recebe uma lista L e retorna a peça faltante do
       quebra-cabeça que não pertence a lista L;
       list -> int'''
    
    maior = 0
    dif = 0
    
    for n in lista_L:
        
        if n > maior:
            
            maior = n
            
    lista_ideal = list(range(1,maior+1))
    
    for n in lista_ideal:
        
        if n not in lista_L:
            
            dif = n
    
    if dif == 0:
        
        dif = maior + 1
    
    return dif