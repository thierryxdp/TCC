def conta_frases(texto):
	l1 = texto.split('. ', texto.count('. '))
    l2 = texto.split('! ', texto.count('! '))
    l3 = texto.split('... ', texto. count('... '))
    l4 = texto.split('? ', texto.count('? '))
    return (len(l1)-1) + (len(l2)-1) + (len(l3)-1) + (len(l4)-1)