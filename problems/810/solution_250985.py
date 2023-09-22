def inverte(frase):
    if str.count(frase,'.')>=1:
        frase = str.strip(frase,'.')
    if str.count(frase,',')>=1:
        frase = str.replace(frase,',','')
    if str.count(frase,'!')>=1:
        frase = str.strip(frase,'!')
    if str.count(frase,'?')>=1:
        frase = str.strip(frase,'?')
    if str.count(frase,'-')>=1:
        frase = str.replace(frase,'-',' ')
    frase[::-1]
    return str.lower(frase)