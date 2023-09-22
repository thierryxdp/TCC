def uppcons(frase):
    vogais = 'AEIOUaeiou'
    posicao = 0
    maiusculas = ''
    while posicao<len(frase):
          if frase[posicao] not in vogais:
            maiusculas = maiusculas + str.upper(frase)[posicao] 
          posicao = posicao + 1
    return maiusculas