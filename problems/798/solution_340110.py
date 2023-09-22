'''função que recebe str e retorna dicionário em que cada str seja chave e tenha um valor o numero de vezes de aparição de palavras'''
def freq_palavras(frases):
    palavras=frases.split()
    dicionario={}
    for i in palavras:
        contador= palavras.count(i)
        dicionaario.update({i:contador})
    return dicionario