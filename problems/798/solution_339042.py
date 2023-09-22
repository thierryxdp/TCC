#EXEMPLO: freq_palavras("dinheiro é dinheiro e vice versa")
#RETORNA O DICIONÁRIO: {"dinheiro":2, "é":1, "e":1, "vice":1, "versa":1}
def freq_palavras(frases):
    """Função que recebe uma string e retorna um dicionário onde cada 
    palavra dessa string seja uma chave e tenha como valor o n°de vezes
    que a palavra aparece;
    str -> dict"""
    dicionario = {}
    lista = str.split(frases)
    
    for palavra in lista:
        if palavra in dicionario:
            dicionario[palavra] = dicionario[palavra] + 1
        else:
            dicionario[palavra] = 1
    
    return dicionario