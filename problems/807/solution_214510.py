def conta_frases(frases):
    '''funcao que conta a quantidade de frases existentes em uma string passada como parametro, baseada na pontuacao
       string -> int'''
    pontofinalespaco = str.count(frases,'. ', 0, -2)
    pontofina = str.count(frases,'.', -2)
    exclamacao = str.count(frases,'!')
    interrogacao = str.count(frases,'?')
    reticencias = str.count(frases,'...')
    quant_frases = pontofinalespaco + pontofinal + exclamacao + interrogacao + reticencias
    return quant_frases