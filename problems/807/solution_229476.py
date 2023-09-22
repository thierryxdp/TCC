def conta_frases(texto):
    '''
    Função que calcula o número de frases em um texto fornecido
    em forma de string. A frase pode ser finalizadada com
    um ponto final, exclamação, interrogação ou tres pontos 
    em sequencia. É dado como entrada uma string.
    str->int 
    '''
    tres_pontos = str.count(texto,'...')
    ponto = str.count(str(str.split(texto,'...')),'.')
    exclamacao = str.count(texto,'!')
    interrogacao = str.count(texto,'?')
    
    
    return (tres_pontos + ponto + exclamacao + interrogacao)