# Calcula a quantidade de frases de um texto
# frase: string
# string -> int
def conta_frases(texto):
    
    """Calcula a quantidade de frases que a string 'texto' tem, considerando como fim de cada frases os
    pontos de exclamação, interrogação, reticências ou ponto final."""

    texto = str.replace(texto, "!", "#")
    texto = str.replace(texto, "?","#")
    texto = str.replace(texto, "...","#")
    texto = str.replace(texto, ".", "#")
    #cada sinal foi substituído por '#' para ficar mais fácil a separação dos termos para a contagem
    #obtive no final um texto onde todos os pontos foram substituidos por '#'

    return len(str.split(texto,"#"))-1