def freq_palavras(frases):
    '''Função que recebe uma frase e retorna um dicionário
    contendo como chaves cada palavra da frase e como valores
    a frequência de cada palavra
    [list] -> {dict}'''
    lista_palavras = str.strip(frases)
    dicionario_frequencia = {}
    for palavra in lista_palavras:
        frequencia = str.count(frases, palavra)
        dicionario_frequencia[palavra] = frequencia}
    return dicionario_frequencia