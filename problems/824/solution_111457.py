def uppCons(frase):
    
    i = 0
    while i < len(frase):
        if frase[i] == 'a' or 'e' or 'i' or 'o' or 'u':
            frase  = frase.replace('b','B')
            frase  = frase.replace('c','C')
            frase  = frase.replace('d','D')
            frase  = frase.replace('f','F')
            frase  = frase.replace('g','G')
            frase  = frase.replace('h','H')
            frase  = frase.replace('j','J')
            frase  = frase.replace('k','K')
            frase  = frase.replace('l','L')
            frase  = frase.replace('m','M')
            frase  = frase.replace('n','N')
            frase  = frase.replace('p','P')
            frase  = frase.replace('q','Q')
            frase  = frase.replace('r','R')
            frase  = frase.replace('s','S')
            frase  = frase.replace('t','T')
            frase  = frase.replace('v','V')
            frase  = frase.replace('x','X')
            frase  = frase.replace('w','W')
            frase  = frase.replace('y','Y')
            frase  = frase.replace('z','Z')
            frase  = frase.replace('ç','Ç')

        i = i + 1