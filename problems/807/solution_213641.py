# Dada a string texto, esta função retorna quantas frases há na string. 
# Neste caso, estamos considerando que cada frase é terminada por reticencias
# ou apenas UM ponto de exclamação, interrogação ou final.
# str -> int
def conta_frases(texto):
    reticencias = texto.count('...',0,len(texto))
    contador = texto.count('!',0,len(texto))
    contador += texto.count('?',0,len(texto))
    pontofinal = texto.count('.',0,len(texto))-3*reticencias
    
    return contador + pontofinal + reticencias