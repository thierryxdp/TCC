def inverte(frase):
    if str.count(frase,'.')>=1:
        frase = str.strip(frase,'.')
    if str.count(frase,',')>=1:
        frase = str.strip(frase,',')
    if str.count(frase,'!')>=1:
        frase = str.strip(frase,'!')
    if str.count(frase,'?')>=1:
        frase = str.strip(frase,'?')
    if str.count(frase,'-')>=1:
        frase = str.replace(frase,'-',' ')
    return str.lower(frase)