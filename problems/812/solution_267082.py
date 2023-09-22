def retira_pontuacao(texto):
    '''A funcao recebe uma frase e substitui todos os seus sinais de pontuacao por
espacos str->str'''
    for i in '?,/:!;-':
        texto=texto.replace(i,' ')
        if '.' and '...' in texto:
            frase1=texto[0:texto.index('.')]
            frase2=texto[texto.index('.')+3:]
            texto=frase1+frase2
    return texto