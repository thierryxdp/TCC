def conta_frases(string):
    frase=str.split(string,'...')
    F1=len(frase)
    frase2=str.split(frase,'.')
    F2=len(frase2)
    frase3=str.split(string,'?')
    F3=len(frase3)
    frase4=str.split(string,'!')
    F4=len(frase4)
    seq_pontos=F2-((3*F1)-1)
    frase_final=(F1-1)+(F2-1)+(F3-1)+(F4-1)
    return frase_final