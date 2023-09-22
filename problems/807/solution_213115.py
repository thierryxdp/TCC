def conta_frases(frase1,frase2,frase3,frase4):
    """ funcao que conta numero de frases e terminadas componto final,
    um ponto de exclamação, um ponto de interrogação ou tres pontos de 
    sequência
    str, str, str, str -> str"""
    frase1= str.format (frase1,'.' )
    frase2= str.format (frase2 , '!')
    frase3= str.format (frase3 , '?')
    frase4= str.format (frase4 , '...')
    return [frase1(), frase2(), frase3(), frase4()]