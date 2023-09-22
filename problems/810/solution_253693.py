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