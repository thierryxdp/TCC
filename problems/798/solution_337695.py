def freq_palavras(frases):
    '''Esta função conta a quantidade de veses que uma palavra foi dita em uma frase 
	str -> dict '''
    palavras=frases.split()
    dicionario={}
    
    for i in range(len(palavras)):
        
        dicionario[palavras[i]]=palavras.count(palavras[i])
        
    return dicionario
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis