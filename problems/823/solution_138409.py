def faltante(lista):
    '''
    função que recebe uma lista de numeros inteiros que representam as peças do quebra cabeças
    nuemradas de 1 a N. Após isso, ela retorna o numero da peça faltante para Joaozinho pedir.
    list -> int
    '''
    
    if 1 not in lista:
        return 1
        
   	x_peca=0
    contador=0
    
    while contador<(len(lista)-1):
        if lista[contador]!=lista[contador+1]-1:
            x_peca=x_peca+(contador+2)
        contador=contador+1
    if x_peca==0:
               return lista[-1]+1
            
    return x_peca