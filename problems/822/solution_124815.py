def repetidos(lista):
    """ Função que, dados uma lista de números e retorna o número
    de vezes que um elemento aparece igual ao anterior
    list -> int"""
  
    ct1 = 0
    ct2=  0

    while ct1 < len(lista):

        if  lista[ct1]==lista[ct1-1]:
            ct2 = ct2 + 1
            
        ct1 = ct1 + 1        
    return ct2