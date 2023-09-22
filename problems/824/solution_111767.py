uppCons(frase):
    i = 0
    fraseFinal = []
    while(i < len(frase)):
        if ((b in frase) or (c in frase) or (d in frase) or (f in frase) or (g in frase) or (h in frase) or (j in frase) or (k in frase) or (l in frase) or (m in frase) or (n in frase) or (p in frase) or (q in frase) or (r in frase) or (s in frase) or (t in frase) or (v in frase) or (w in frase) or (x in frase) or (z in frase):
			fraseFinal[len(fraseFinal):len(fraseFinal)] = [str.upper(frase[i])]
        else:
            fraseFinal[len(fraseFinal):len(fraseFinal)] = [frase[i]]
        
        i += 1
    
     str.join(fraseFinal,'')
     return fraseFinal