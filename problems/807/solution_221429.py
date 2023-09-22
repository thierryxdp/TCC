def conta_frases(texto):
    """Dado um texto a função conta o número de frases que aparecem
    	no texto, separadas pelas pntuações '.','...','!','?' 
        str-->int"""
    texto1=str.split(texto,'...')
    a=''.join(texto1)
    texto2=str.split(texto1,'.') 
    texto3=str.split(texto1,'!')
    texto4=str.split(texto1,'?')

    return (len(texto1)-1)+(len(texto2)-1)+(len(texto3)-1)+(len(texto4)-1)