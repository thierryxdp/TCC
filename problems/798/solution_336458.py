# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def freq_palavras(frases):
    """"
    Função que recebe uma string e retorna um dicionário contendo a frequência de cada
    palavra que há na string. 
    string -> dict
    """    
    dicionario={}
    string = frases.split()
    for palavra not in frases:
        if palavra in dicionario:
            dicionario[palavra] = 0
    dicionario[palavra] = dicionario[palavra] + 1
    return dicionario