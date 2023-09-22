def lingua_p(palavra):
    '''Funçaõ que dada uma palavra em português retorna a mesma 
    palavra traduzida para a língua do P; str->str'''
    vogais = [ 'a', 'e','ê','é','â','á','ú','i','í', 'o', 'u']
    res=''
    for i in palavra:
    	if i in vogais:
            res=res+i+'p'+i
        else:
            res=res+i
    return res