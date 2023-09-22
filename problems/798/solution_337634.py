# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    '''
    Essa função recebe um string frases e retorna u dicionário cujas entradas são as
    palvras nas frases e os valores são a frequência de cada palavra
    
    str -> dict
    '''
    freq={}
    palavra=''
    for i in range(len(frases)):
        if frases[i] not in ' ':
            palavra=palavra+frases[i]
        elif len(palavra)>0:
            if palavra in list(dict.keys(freq)):
                freq[palavra]=freq[palavra]+1
            else:
                freq[palavra]=1
            palavra=''
    if len(palavra)>0:
            if palavra in list(dict.keys(freq)):
                freq[palavra]=freq[palavra]+1
            else:
                freq[palavra]=1
            palavra=''
    return freq