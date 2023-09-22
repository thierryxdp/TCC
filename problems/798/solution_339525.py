# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    """
    função que recebe uma string e retorna um dicionário
    onde cada palavra dessa string é uma chave e tem como valor
    o número de vezes que a palavra aparece
    str -> dict
    """
    
    dicionario={}
    listinha = frases.split()
    for palavra in listinha:
        if palavra in listinha:
            dicionario[palavra] = listinha.count(palavra)
    return dicionario