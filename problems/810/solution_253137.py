def retira_pontuacao(texto):
    '''A funcao recebe uma frase e substitui todos os seus sinais de pontuacao por
espacos str->str'''
    for i in '?,/:!;-.':
        texto=texto.replace(i,' ')
    return texto


def inverte(frase):
    '''A funcao recebe uma frase como entrada e retorna uma frase com a ordem das palavras
invertida str->str'''
    pequeno=frase.lower()
    semponto=retira_pontuacao(pequeno)
    lista=semponto.split()
    lista.reverse()
    return ' '.join(lista)