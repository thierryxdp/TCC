def filtra_pares(tupla):
    '''recebe uma tupla com quatro elementos inteiros
como parâmetro, e retorna uma nova tupla contendo apenas
os elementos pares da tupla originial, 
na mesma ordem em que se encontravam.
tupla->tupla'''
    tuplaF=()
    
    if tupla[0]%2==0:
        tuplaF=tuplaF+(tupla[0],)
        
    if tupla[1]%2==0:
        tuplaF=tuplaF+(tupla[1],)
    
    if tupla[2]%2==0:
        tuplaF=tuplaF+(tupla[2],)
        
    if tupla[3]%2==0:
        tuplaF=tuplaF+(tupla[3],)
        
    return tuplaF