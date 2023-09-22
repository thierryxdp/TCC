def lingua_p (palavra):
    '''Função retorna a palavra na lingua do P (é inserida a letra 'p' +vogal).
    str -> str'''
    traducao = ''
    for i in palavra:
        if i in 'AEIOUaeiouáàãâéèêíìîóòôõúùû':
            traducao = traducao + i + 'p' + i
        else:
            traducao = traducao +i
    return traducao