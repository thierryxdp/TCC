def uppCons(frase):
    '''
    	Função que recebe como parâmetro
        de entrada uma frase e retorna
        essa mesma frase, porém com as
        consoantes em maiúsculo
        : param frase: str
        : return: str
    '''
    indice = 0
    frase_cons_maiusc = ''
    
    while indice < len(frase):
        if frase[indice] in 'ÁÉÍÓÚÃÕÂÊAEIOUáéíóúãõâêaeiou,;:.—-?! ':
            frase_cons_maiusc += frase[indice]
        else:
            frase_cons_maiusc += str.upper(frase[indice])
        
        indice += 1
    
    return frase_cons_maiusc