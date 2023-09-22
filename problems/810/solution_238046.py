def inverte(frase):
    """ Dada uma frase qualquer vamos remover as pontuacoes da frase incluindo
        travessão, virgula, dois pontos, ponto e virgula, ponto final, vamos
        substituiras letras maisculas pelas minusculas e por fim inverter a
        frase.
        entrada ---> str
        saida   ---> str  """
    frase = frase.replace("-"," ")
    frase = frase.replace(","," ")
    frase = frase.replace(":"," ")
    frase = frase.replace(";"," ")
    frase = frase.replace("."," ")
    frase = frase.replace("?"," ")
    frase = frase.replace("!"," ")
    frase = str.lower(frase)
    frase = frase.split()
    frase = frase[::-1]
    frase = "".join(frase)
    return frase


""" teste
    resultados esperados:
    resultados obtidos: """