def primo(num):
    
    ''' Função que, dado um número inteiro positivo,
        verifica se esse número é primo ou não.
        int -> bool '''
    
    resposta = True
    
    for elemento in range(2,num):
        if num%elemento == 0:
            resposta = False
            
    return resposta