def primo(numero):
    '''
       funcao que retorna se o numero dado como entrada e
       primo ou nao
       int -> bool 
    '''
    resposta = True 
    for i in list(range(2,numero)):
        if numero%i==0:
             resposta = False
    return resposta