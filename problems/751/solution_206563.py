def quant_palavras(frase):
    """Função que dada uma frase, retorna o número de palavras da frase,
       considerando possíveis espaçõs vazios.
       str->int
       
       Parâmetros:
       frase: frase que será contabilizado o número de palavras da frase.
       
       returns: O número de palavras da frase.
    """
    if frase[0] == "" and frase[-1] == "":
        return str.count(frase,"")-1
    elif frase[0] =="":
        return str.count(frase,"")
    else:
        return str.count(frase,"")+1