def separa_palavras(frases):
    """Essa função já foi usada como exercício antes e ela pega uma
    frase e a 'ajeita' tirando os espaços do começo e do fim
    assinatura: str---> str"""
    frases1 = frases.split(' ')
    if frases1[0]=='':
        del frases1[0]
    if frases1[-1]=='':
        del frases1[-1]
    return frases1

def freq_palavras(frases):
    """ Essa função (freq_palavras) pega uma string com um 
    texto e devolve um dicionário que relaciona a palavra 
    com a quantidade de vezes que ela aperece.
   
   assinatura: string----> dicionário
   """
    dicionario = {}
    frases = frases.split()
    for i in range(len(frases)):
        dicionario[frases[i]] = frases.count(frases[i])
    return dicionario