# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    '''
        recebe uma string contendo uam frase e retorna um dicionario onde
        cada palavra da frase e uma chave que tem como valor o numero de
        repeticoes da palavra que figura como chave
        entrada: string
        saida: dicionario
    '''
    dfreq_pal = {}
    lista_palavras = str.split(frases, ' ')
    for chq_chave in range(len(lista_palavras)):
        if lista_palavras[chq_chave] not in dict.keys(dfreq_pal):
            dfreq_pal[lista_palavras[chq_chave]] = 1
        else:
            dfreq_pal[lista_palavras[chq_chave]] = dfreq_pal[lista_palavras[chq_chave]] + 1
    return dfreq_pal