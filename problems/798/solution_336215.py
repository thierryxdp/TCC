# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    '''
    	Fucao recebe uma string e retorna um dicionario
        cujas chaves correspondem às palavras da string dada
        e cujos valores sao o numero de vezes que cada palavra
        aparece
        str -> dict
        
    '''
    Lpalavras = frases.split(' ')
    dicio = {}
    for palavra in Lpalavras:
        
        Lpalavras.count(palavra) = freq_palavra
        dicio[palavra] = Lpalavras.count(palavra)
                 
    return dicio