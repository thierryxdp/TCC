def uppcons(frase):
    vogais = 'AEIOUaeiou'
    posicao = 0
    maiúsculas = ''
    while posicao<len(frase):
          if frase[posicao] not in vogais:
            maiúsculas = maiúsculas + str.upper(frase)[posicao] 
          posicao = posicao + 1
    return maiúsculas