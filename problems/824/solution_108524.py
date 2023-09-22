def uppCons(frase):
    c=o
    cons= ''
    
    while c < len(frase):
        if frase[c] in 'qiwduqjibchqbwjqa':
            cons=cons+str.upper(frase[c])
        else:
            cons=cons + frase[c]
        c=c+1
	return cons