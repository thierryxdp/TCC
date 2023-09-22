def retira_pontuacao(x):
    '''Retira caracteres que representam
    pontuação os trocando por um espaço'''

    ret = str.replace(x, '...', ' ')
    pt = str.replace(ret, '.', ' ')
    inte = str.replace(pt, '?', ' ')
    exclama = str.replace(inte, '!', ' ')
    virg = str.replace(exclama, ',', ' ')
    travessao = str.replace(virg, '-', ' ')
    doispt = str.replace(travessao, ':', ' ') 
    pontoevirg = str.replace(doispt, ';', ' ')

    return pontoevirg