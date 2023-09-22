def conta_frases(frases):
    '''funcao que conta a quantidade de frases existentes em uma string passada como parametro, baseada na pontuacao
       string -> int'''
    pontofinalespaco = str.count(frases,'. ', 0, -3)
    pontofinal = str.count(frases, '.', -1)
    exclamacao = str.count(frases, '!')
    interrogacao = str.count(frases, '?')
    quant_frases = pontofinalespaco + pontofinal + exclamacao + interrogacao
    return quant_frases