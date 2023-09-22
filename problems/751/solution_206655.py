def quant_palavra(frase):
    """ dada uma frase qualquer, vamos contar e retonar quantas palavras fazem
        parte dessa frase. considere que a frase pode ter espaço no começo e
        no final
    .
    entrada --> str
    saida   --> int  """
    frase = str.split(frase)
    return len(frase)


""" teste
    resultados esperados:
    resultados obtidos: """