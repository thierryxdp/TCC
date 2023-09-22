def uppCons(frase):
	i = 0
	con = ''
	while i<len(frase):
        if frase[i] in 'b':
            con=con + frase.replace(frase[i],'B')
        elif frase[i] in 'c':
            con = con + frase.replace(frase[i],'C')
        if frase[i] in 'd':
            con = con + frase.replace(frase[i],'D')
        if frase[i] in 'f':
            con = con + frase.replace(frase[i],'F')
        if frase[i] in 'g':
            con = con + frase.replace(frase[i],'G')
        if frase[i] in 'h':
            con = con + frase.replace(frase[i],'H')    
        if frase[i] in 'j':
            con = con + frase.replace(frase[i],'J')   
        if frase[i] in 'k':
            con = con + frase.replace(frase[i],'K')
        if frase[i] in 'l':
            con = con + frase.replace(frase[i],'L')
        if frase[i] in 'm':
            con = con + frase.replace(frase[i],'M')
        if frase[i] in 'n':
            con = con + frase.replace(frase[i],'N')
        if frase[i] in 'p':
            con = con + frase.replace(frase[i],'P')
        if frase[i] in 'q':
            con = con + frase.replace(frase[i],'Q')
        if frase[i] in 'r':
            con = con + frase.replace(frase[i],'R')
        if frase[i] in 's':
            con = con + frase.replace(frase[i],'S')
        if frase[i] in 't':
            con = con + frase.replace(frase[i],'T')
        if frase[i] in 'v':
            con = con + frase.replace(frase[i],'V')
        if frase[i] in 'w':
            con = con + frase.replace(frase[i],'W')
        if frase[i] in 'x':
            con = con + frase.replace(frase[i],'X')
        if frase[i] in 'y':
            con = con + frase.replace(frase[i],'Y')
        if frase[i] in 'z':
            con = con + frase.replace(frase[i],'Z')
        i+=1
    
    return con