def lingua_p(palavra):
    '''Função que recebe uma palavra em português e retorna ela traduzida para a língua do p
    str -> str'''
    traducao = ''
    for i in palavra:
        if i in 'aeiouAEIOU':
            traducao = traducao + 'p' + i + 'p'
        else:
            traducao = traducao + i
	return traducao