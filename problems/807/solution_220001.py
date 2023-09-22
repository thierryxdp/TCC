def conta_frases(texto:str)->str:
    "Dado um texto, contar as frases."
    numeroFrase = texto.count('!')
    numeroFrase += texto.count('?')
    numeroFrase += texto.count('...')
    numeroFrase += texto.count('.')
    
    numeroFrase -=  texto.count('...')*2
    
    return numeroFrase