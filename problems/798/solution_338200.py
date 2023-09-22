def freq_palavras(frases):
    """Recebe uma string e retorna um dicionário em que cada palavra
    da string é uma chave e seu valor é o númerp de vezes que a 
    palavra aparece na string.
    assinatura: string --> dict
    testes:
    """
    contador = 0 
    acumulador = {}
    for i in frases:
        if i == frases[i]:
            acumulador = {}
            acumulador[frases[i]] == contador + 1
    return acumulador