def conta_frases (texto:str) ->str :
    "recebe um texto e conta o número de frases que aparece nele"
    
    #Fazendo o backup do texto original
    #textoAlterado = texto
    
    #contabilizado as pontuaçoes
    numeroFrase = texto.count('!')
    numeroFrase += texto.count('?')
    numeroFrase += texto.count('.')
    numeroFrase += texto.count('...')
    
    #compensando a triplicidade das reticencias
    numeroFrase -= texto.count('...')*3
    return numeroFrase