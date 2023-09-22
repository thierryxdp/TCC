def retira_pontuacao(frase):
    '''Função que retorna a frase dada substituindo os caracteres por espaços'''
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
    if '''!''' in frase:
        frase=str.replace(frase,'''!''',''' ''')
    if '''?''' in frase:
        frase=str.replace(frase,'''?''',''' ''')
    return frase

def inverte(frase):
    '''Função que dada uma frase retorne uma outra frase contendo as mesmas palavras de entrada na ordem inversa, em letras minúsculas e sem pontuação
    str->str'''
    frase=retira_pontuacao(frase)
    a=str.lower(a)
    a=frase.split(''' ''')
    a=a[::-1]
    return str.join(''' ''',a)