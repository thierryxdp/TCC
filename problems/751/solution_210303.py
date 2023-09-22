def quant_palavras(frase):
    """ Dada uma frase no formato de string essa função retorna a quantidade
    de palavras na frase. Foram considerados para retirarmos os espaços no
    inicio e no final da frase, pois se não eles seriam considerados como
    palavras a mais.
    assinatura: str---> int
    teste:
    quant_palavras('To fazendo computação')==3
    quant_palavras(' To fazendo computação ')==3
    quant_palavras(' To fazendo computação')==3
    quant_palavras('To fazendo computação ')==3
    """
    frase1= str.split(frase, " ")
    if frase1[0] == '':
        del frase1[0]
    if frase1[-1] == '':
        del frase1[-1]
        
    return len(frase1)