def conta_frases(texto):
    'retorna a quantidade de frases no texto digitado....string---int'
    texto=texto.replace('!','.').replace('?','.').replace('...','.')
    frases=texto.split('. ')
    return len(frases)