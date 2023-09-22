def one(a):
     'subtrai a quantidade de pontos pela quantidade de reticencias'
     'entrada: str'
     'saida: int'
    if '...' in a:
        return str.count(a,'...')+str.count(a,'...')
    else:
          return 0
def three(a):
    'conta quantos pontos existem na frase'
    'entrada: str'
    'saida: int
    if '.'in a:
        return str.count(a,'.')
    else:
          return 0    
def conta_frases(frase):
    'retorna a quantidade de uma frases'
    'entrada: str'
    'saida: int'
    return (-1)*one(frase)+str.count(frase,'!')+str.count(frase,'?')+three(frase)