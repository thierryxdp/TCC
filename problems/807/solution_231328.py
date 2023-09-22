def conta_frases(texto):
    """Função que dado um texto armazenado em uma string, conta o n° de 
    frases que aparecem neste texto;
    str -> int"""
    interrog = srt.count(texto,'?')
    exclam = srt.count(texto,'!')
    ponto = str.count(texto,'.')
    reticent = str.count(texto,'...')
    return (ponto-reticent*3+exclam+interrog+reticent)