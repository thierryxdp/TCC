def qtd_dividores(numero):
    '''retorna os números que são divisores do número dado''' 
    '''int -> int,int,...'''
    
    divisores=[]
    inteiro=1
    
    while inteiro <= numero:
        if numero%inteiro == 0:
            divisores=divisores+inteiro
            inteiro=inteiro+1
        
        return divisores