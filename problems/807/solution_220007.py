def conta_frases(texto:str)->str:
    "Dado um texto, contar as frases."
    textoAlterado = texto.replace('...','#')
    
    numeroFrase = textoAlterado.count('!')
    numeroFrase += textoAlterado.count('?')
    numeroFrase += textoAlterado.count('#')
    numeroFrase += textoAlterado.count('.')
      
    return numeroFrase