def maiores (inteiros,n):
    '''retorna outra lista com os numeros da original em ordem crescente maiores que n'''
    '''list,str -> list'''
    
    inserido = list.append(inteiros,n)
    crescente = sorted(inserido)  
    
    return crescente