def inverte(frase):
    '''
    Função subistitui toda pontuação da frase por espaço ''
    e inverte a frase.
    str -> str
    '''
    pFinal = str.join('', str.split(frase, '.'))
    virg = str.join('', str.split(pFinal, ','))
    interroga = str.join('', str.split(virg, '?'))
    exclama = str.join('', str.split(interroga, '!'))
    trave = str.join('', str.split(exclama, '-'))
    particiona = trave.split('')
    inverso = particiona[-1:-(len(particiona)+1):-1]
    une = str.strip(str.join(' ',inverso))
    return une