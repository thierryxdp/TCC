def retira_pontuacao(texto):
    '''A funcao recebe uma frase e substitui todos os seus sinais de pontuacao por
espacos str->str'''
    for i in '?,/:!;-.':
        texto=texto.replace(i,' ')
    return texto