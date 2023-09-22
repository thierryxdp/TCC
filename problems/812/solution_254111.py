def retira_pontuacao(frase):
    '''Função que retorna a frase dada substituindo os caracteres de pontuação por espaço
    str->str'''
    if ''',''' in frase:
        frase=str.replace(frase, ''',''',''' ''')
    if '''-''' in frase:
        frase=str.replace(frase,'''-''',''' ''')
    if ''':''' in frase:
        frase=str.replace(frase,''':''',''' ''')
    if ''';''' in frase:
        frase=str.replace(frase,''';''',''' ''')
    if '''.''' in frase:
        frase=str.replace(frase,'''.''',''' ''')
    return frase