def uppCons(frase):
    """Dada uma frase, a função retorna a frase com todas as
    suas consoantes em maiúsculas e os demais caracteres
    exatamente como estavam na frase original.
    Parametros de Entrada: str
    Retorna: str"""
    
    auxiliar=''
    i=0

    while i< len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWYZXÇbcdfghjklmnpqrstvwyxzç':
            auxiliar= auxiliar + frase[i].upper()
            i=i+1
        else:
            auxiliar= auxiliar+ frase[i]
            i=i+1
    return auxiliar