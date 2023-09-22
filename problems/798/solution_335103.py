def freq_palavras(frases):
    dicionario = {}
    n = 1
    
    for p in str.split(frases,' '):
        	if p in dicionario: 
            	dicionario[p] = dicionario[p] +1
            elif p not in dicionario:
                dicionario[p] = n
                
    return dicionario# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis