def freq_palavras(frases):
    ''' '''
    palavras=frases.split()
    dicionario={}
    
    for i in range(len(palavras)):
        
        dicionario[palavras[i]]=palavras.count(palavras[i])
        i+=1
    return dicionario
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis