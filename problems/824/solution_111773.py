def uppCons(frase):
    i = 0
    fraseFinal = []
    while(i < len(frase)):
        if (('b' in frase[i]) or ('c' in frase[i]) or ('d' in frase[i]) or ('f' in frase[i]) or ('g' in frase[i]) or ('h' in frase[i]) or ('j' in frase[i]) or ('k' in frase[i]) or ('l' in frase[i]) or ('m' in frase[i]) or ('n' in frase[i]) or ('p' in frase[i]) or ('q' in frase[i]) or ('r' in frase[i]) or ('s' in frase[i]) or ('t' in frase[i]) or ('v' in frase[i]) or ('w' in frase[i]) or ('x' in frase[i]) or ('z' in frase[i])):
			fraseFinal[len(fraseFinal):len(fraseFinal)] = [str.upper(frase[i])]
        else:
            fraseFinal[len(fraseFinal):len(fraseFinal)] = [frase[i]]
        
        i += 1
    
	fraseFinal = str.join(fraseFinal,'')
    return fraseFinal