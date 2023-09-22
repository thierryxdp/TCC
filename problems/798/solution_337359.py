# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    ''' ...
    str --> dict '''
    
    freq = dict ()
    palavras = str.split(frases, ' ')
    
    for palavra in palavras:
        if palavra in freq:
            # Se a palavra já existe, soma 1
            freq[palavra] += 1
            
        else:
            # Se a palavra não existe, é a primeira, logo 1
            freq[palavra] = 1
        
        return freq