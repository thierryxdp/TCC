def acima_da_media(numero):
    ''' Essa função calcula a média de uma lista, voltando os valores acima da media. lista, list'''
    
    soma = sum(numero)
    
    x = len(numero)
    
    media = soma/x
    
    
    return maiores(numero,media)