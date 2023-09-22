def uppCons(frase):
    '''eae'''
    i=0
    frasef:''
    vogais="aeiouAEIOU"
    while i<len(frase):
        if frase[i] != vogais:
        	frase=frase[i].upper() + frasef
        if frase[i] == vogais:
            frase=vogais
        i=i+1
    return frasef