def freq_palavras(frases):
    ''' '''
    palavras=frases.split()
    dicionario={}
    i=0
    for i in range(len(palavras)):
        print('i', i)
        dicionario[palavras[i]]=palavras.count(palavras[i])
        i+=1
    return dicionario
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis