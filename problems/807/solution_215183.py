def conta_frases(frase):
    """ dada uma frase qualquer vamos contar quantas palavras aparecem no texto
        as frases são terminadas por: ponto final, exclamcao,interrogação
         ou reticencias
        entrada -->str
        saida   --> int  """
    frase1 = frase.replace("...","!")
    frase2 = frase1.replace("?","!")
    frase3 = frase2.replace(".","!")
    return len(frase3.split("!"))-1