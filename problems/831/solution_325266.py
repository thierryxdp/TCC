def lingua_p(palavra):
	'''Função que dada uma palavra, retorna a mesma traduzida para
	a língua do p, que corresponde a letra p e a mesma vogal inseridas
	após todas as vogais da	palavra, com todas as letras minúsculas.
	Entrada: string
	Saída: string'''
    palavra=str.lower(palavra)
    analisada=''
    for caractere in palavra:
        if caractere in 'aàáâãeèéêiìîíoôõuúùû':
            analisada+=caractere+'p'
        analisada+=caractere
    return analisada