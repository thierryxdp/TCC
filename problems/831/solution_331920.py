def lingua_p(palavra):
    ''''''
    nova= '' 
    for l in palavra:
    	if l in 'aeiouáéúí':
            nova= nova + l + 'p' + l
        else: 
            nova=nova + l
    return nova