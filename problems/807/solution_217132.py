def conta_frases(frase):
    """ funcao que conta numero de frases e terminadas componto final,
    um ponto de exclamação, um ponto de interrogação ou tres pontos de sequência
    str, str, str, str -> int"""
    frase= str.replace (frase,'.', '#')
    frase= str.replace (frase,'!','#' )
    frase= str.replace (frase,'?','#' )
    frase= str.replace (frase,'...','#' )
    return len(str.split(frase,'#'))-1