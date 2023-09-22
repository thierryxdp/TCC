def conta_frases(texto):
    ''''função que recebe um string e conta a recorrência de certos carácteres que indiquem o
    fim de uma frase. Recebe string e devolve int.'''
    num = texto.count('.') + texto.count('!') + texto.count('?')
    for i in range(len(texto)):
        if texto[i:i+3] == '...':
            num -= 2
    return num