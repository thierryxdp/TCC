def retira_pontuacao(x):
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
    '''assinatura: str > str
    casos de teste: inverte('oi, bom') ==bom oi
    inverte('muito bem') ==bem muito
    inverte('voce está bem?') ==bem está voce'''
    frase = str.lower(x)
    frase_sempt = retira_pontuacao(frase)
    frase_corta = str.split(frase_sempt,)
    lista_inv = list.reverse(frase_corta)
    frase_inv = str.join(' ', frase_corta)

    return frase_inv