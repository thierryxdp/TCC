def retira_pontuacao(x):
    '''Retira caracteres que representam pontuação os trocando por um espaço'''

    ret = str.replace(x, '...', ' ')
    pt = str.replace(ret, '.', ' ')
    inte = str.replace(pt, '?', ' ')
    exclama = str.replace(inte, '!', ' ')
    virg = str.replace(exclama, ',', ' ')
    travessao = str.replace(virg, '-', ' ')
    doispt = str.replace(travessao, ':', ' ') 
    ptvirg = str.replace(doispt, ';', ' ')

    return ptvirg

def inverte(x):
	''' str > str
    Dada uma frase, retorna outra frase que inverta a ordem dessas palavras e retira qualquer pontuação, caso exista.'''
    frase = str.lower(x)
    frase_sempt = retira_pontuacao(frase)
    frase_corta = str.split(frase_sempt,)
    lista_inv = list.reverse(frase_corta)
    frase_inv = str.join(' ', frase_corta)

    return frase_inv