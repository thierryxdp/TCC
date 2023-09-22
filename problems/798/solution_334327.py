def freq_palavras(frases):
    '''Função que recebe uma frase e retorna um dicionário
    contendo como chaves cada palavra da frase e como valores
    a frequência de cada palavra
    [list] -> {dict}'''
    lista_palavras = str.split(frases)
    dicionario_frequencia = {}
    for palavra in lista_palavras:
        if len(palavra) > 1:
            frequencia = str.count(frases, palavra)
        	dicionario_frequencia[palavra] = frequencia
        else: 
            frequencia = str.count(frases, ' ' + palavra + ' ')
        	dicionario_frequencia[palavra] = frequencia
    return dicionario_frequencia