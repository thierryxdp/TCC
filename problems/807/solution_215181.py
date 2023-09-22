def conta_frases(frase):
    """ dada uma frase qualquer vamos contar quantas palavras aparecem no texto
        as frases são terminadas por: ponto final, exclamcao,interrogação
         ou reticencias
        entrada -->str
        saida   --> int  """
    fraseA = frase.replace("...","!")
    fraseB = frase.replace("?","!")
    fraseC = frase.replace(".","!")
    return len(fraseC.split("!"))-1



""" teste
    resultados esperados:
    resultados obtidos: """