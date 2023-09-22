def retira_pontuacao(frase):
    '''
    Função subistitui toda pontuação da frase por espaço ''.
    str -> str
    '''
    pFinal = str.join(' ', str.split(frase, '.'))
    virg = str.join(' ', str.split(pFinal, ','))
    interroga = str.join(' ', str.split(virg, '?'))
    exclama = str.join(' ', str.split(interroga, '!'))
    trave = str.join(' ', str.split(exclama, '-'))
    return trave