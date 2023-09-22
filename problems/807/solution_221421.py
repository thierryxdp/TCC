def conta_frases(texto):
    """Dado um texto a função conta o número de frases que aparecem
    	no texto, separadas pelas pntuações '.','...','!','?' 
        str-->int"""
    texto1=str.split(texto,'...')
    n1=(len(texto1)-1)
    a=''.join(texto1)
    texto2=str.split(texto1[0],'.')
    n2=len(texto2)-1
    texto3=str.split(texto1[0],'!')
    n3=len(texto3)-1
    texto4=str.split(texto1[0],'?')
    n4=len(texto4)-1
    return n1+n2+n3+n4