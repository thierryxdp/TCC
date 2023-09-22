def posLetra(frase,letra,ocorrencia):
    '''retorna em que posição da string a ocorrência da letra está.
    str, str, int -> int'''
    
    i=0
    
    while i<len(frase):
        if frase[i]==letra: