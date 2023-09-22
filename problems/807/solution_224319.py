def conta_frases(frase):
    'retorna a quantidade de uma frases'
    'entrada: str'
    'saida: int'
    if '...' in frase:
        return str.count(frase,'...')+str.count(frase,'!')+str.count(frase,'?')
    elif '.' in frase: 
         return +str.count(frase,'!')+str.count(frase,'?')+str.count(frase,'.')