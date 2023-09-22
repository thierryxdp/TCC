def conta_frases(texto):
    if len(texto.split('.',))==1:
        return 1
    if len(texto.split('.',))>1:
        return len(texto.split('.'))-1
    if '...' in texto:
        return len(texto.split('.'))-4