def conta_frases(frase):
    '''
    Ao inserir uma string com várias frases, o código 
    retorna quantas frases possuem baseado na quantidade
    de pontos, interrogações, exclamações e reticências.
    str -> int
    '''
    return str.count(frase,".") + str.count(frase,"?") + str.count(frase,"!")- + str.count(frase,"...")*2