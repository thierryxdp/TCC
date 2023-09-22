#Funcao que recebe uma string onde cada palavra dessa string vira um dicionario que conta as repeticoes
#O valor de entrada eh uma string e o de retorno eh um dicionario

def freq_palavras(frases):
    d1 = {}
    frases0 = str.split(frases,' ' )
    i = 0
    while i<len(frases0):
     if frases0[i] not in d1:
      d1[frases0[i]] = 0
     d1[frases0[i]] = d1[frases0[i]] + 1
     i = i + 1
    return d1