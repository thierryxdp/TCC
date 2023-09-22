# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    '''
    Recebe um texto, separa em palavras e conta a frequencia de palavras
    Retorna um dicionario contendo a palavra como chave e a frequencia de ocorrência como valores do dicionario
    '''
    frases = frases.lower()
    dic = {}
    palavras = frases.split()
    for palavra in palavras:
        if palavra in dic:
            dic[palavra] += 1
        else:
            dic[palavra] = 1
    return dic