def one(a):
    if '...' in a:
        return str.count(a,'...')
    else:
          return 0
def three1(a):
    if '. 'in a:
        return str.count(a,'. ')
    else:
          return 0    
def negativo(a):
    if '... ' in a:
        return str.count(a,'... ')*(-1)
    else:         
          return 0
def conta_frases(frase):
    'retorna a quantidade de uma frases'
    'entrada: str'
    'saida: int'
    return (one(frase))+str.count(frase,'!')+str.count(frase,'?')+(three1(frase))+negativo(frase)