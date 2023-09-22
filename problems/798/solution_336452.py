# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def freq_palavras(frases):
    """"
    Função que recebe uma string e retorna um dicionário contendo a frequência de cada
    palavra que há na string. 
    string -> dict
    """
    
    dicionario={}
    
    for palavra in frases:
        if not palavra in dicionario:
            dicionario[palavra] = frases.count(palavra)
    return dicionario