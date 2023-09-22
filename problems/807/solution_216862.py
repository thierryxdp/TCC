def conta_frases(texto):
    ''''função que recebe um string e conta a recorrência de certos carácteres que indiquem o
    fim de uma frase. Recebe string e devolve int.'''
    num = texto.count('. ') + texto.count('!') + texto.count('?') + texto.count('...')
    return num