def lingua_p(palavra):
    '''Função que recebe uma string, 
    retorna a mesma palavra traduzida na língua do P'''
    palavra = palavra.lower()
    nova_palavra = ''
    for i in palavra:
        if i in 'aáàâãeéiíoóôõú':
            nova_palavra += i + 'p' + i
        else:
            nova_palavra += i
	return nova_palavra