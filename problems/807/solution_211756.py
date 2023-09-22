def conta_frases(texto):
    ''' conta_frase recebe um texto e devolve quantas frases o texto possui.
    Cada Frase no texto é terminada com um ponto final, um ponto de excalmação, um ponto de interrogação ou três pontos em sequência(reticências).
    Pontos de exclamação ou de interrogação não podem aparecer repetidos em sequência no texto.
    str-->int.'''
    texto=str.replace(texto,"!","/")
    texto=str.replace(texto,"...","/")
    texto=str.replace(texto,".","/")
    texto=str.replace(texto,"?","/")
    texto=str.split(texto,"/")
    return len(texto)-1