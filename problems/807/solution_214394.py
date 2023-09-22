def conta_frases(texto):
    """função que conta o numero de frases que aparecem em um texto.
    str->int"""
    if str.find(texto,'!')==-1 and str.find(texto,'?')==-1:
        ponto=str.split(texto, '.')
        frases=len(ponto)
        return frases
    
    elif str.find(texto, '!')!=-1 and str.find(texto,'?')==-1:
        ponto=str.split(texto, '.')
        ex=str.split(ponto, '!')
        frases= len(ex)
        return frases
   
    elif str.find(texto, '!')==-1 and str.find(texto,'?')!=-1:
        ponto=str.split(texto, '.')
        inter=str.split(ponto, '?')
        frases= len(inter)
        return frases
    
    elif str.find(texto, '!')!=-1 and str.find(texto,'?')!=-1:
        ponto=str.split(texto, ('.','!','?'))
        frases=len(ponto)
        return frases