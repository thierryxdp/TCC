def uppcons(frase):
    vogais = 'AEIOUaeiou'
    posição = 0
    maiúsculas = ''
    while posição<len(frase):
          if frase[posição] not in vogais:
            maiúsculas = maiúsculas + str.upper(frase)[posição] 
          posição = posição + 1
    return maiúsculas