def conta_frases(texto):
    """função que conta o numero de frases que aparecem em um texto.
    str->int"""
    if str.find(texto,'!')==-1 and str.find(texto,'?')==-1:
        ponto final=str.split(texto, '.')
        frases=len(ponto final)
        return frases
    
    elif str.find(texto, '!')!=-1 and str.find(texto,'?')==-1:
        ponto final=str.split(texto, '.')
        ponto ex=str.split(ponto final, '!')
        frases= len(ponto ex)
        return frases
   
    elif str.find(texto, '!')==-1 and str.find(texto,'?')!=-1:
        ponto final=str.split(texto, '.')
        ponto inter=str.split(ponto final, '?')
        frases= len(ponto inter)
        return frases
    
    elif str.find(texto, '!')!=-1 and str.find(texto,'?')!=-1:
        ponto final=str.split(texto, '.')
        ponto inter=str.split(ponto final, '?')
        ponto ex=str.split(ponto inter,'!')
        frases= len(ponto ex)
        return frases