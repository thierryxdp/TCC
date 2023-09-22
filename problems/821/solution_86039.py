def fatorial(numero):
    """recebe um numero e calcula o
fatorial desde numero"""
    primeiro = 1 
    fatorial = 1 #primeira resposta
    
    while primeiro <= numero:
        fatorial = fatorial*primeiro #produzindo o processo fatorial
        primeiro = primeiro + 1 #indo para o proximo numero

    return fatorial