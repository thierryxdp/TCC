def retira_pontuacao(x):
    '''função que retira as pontuações e substitui por espaço.
    assinatura: str > str
    casos de teste:retira_pontuacao('O ignorante afirma, o sábio duvida, o sensato reflete.') ==O ignorante afirma  o sábio duvida  o sensato reflete
    retira_pontuacao('oi,tchau!') ==oi tchau'''
    ret = str.replace(x, '...', ' ')
    pt = str.replace(ret, '.', ' ')
    inte = str.replace(pt, '?', ' ')
    exclama = str.replace(inte, '!', ' ')
    virg = str.replace(exclama, ',', ' ')
    travessao = str.replace(virg, '-', ' ')
    doispt = str.replace(travessao, ':', ' ')
    ptvirg = str.replace(doispt, ';', ' ')

    return ptvirg