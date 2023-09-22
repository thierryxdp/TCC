#EXEMPLO: freq_palavras("dinheiro é dinheiro e vice versa")
#RETORNA O DICIONÁRIO: {"dinheiro":2, "é":1, "e":1, "vice":1, "versa":1}
def freq_palavras(frases):
    """Função que recebe uma string e retorna um dicionário onde cada 
    palavra dessa string seja uma chave e tenha como valor o n°de vezes
    que a palavra aparece;
    str -> dict"""
    dicionario = {}
    listadecompras = str.split(frase)
    
    for palavra in listadecompras:
        if palavra in dicionario:
            dicionario{palavra} = dicionario(palavra} + 1
        else:
            dicionario{palavra} = 1
             if frase in dicionario{palavra}:
                dicionario = dicionario +{palavras}
                                             
    return dicionario