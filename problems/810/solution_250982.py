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
    frase = str.split(frase)
    frase = list.reverse(frase)
    frase = list.sum(frase)
    frase = str(frase)
    return str.lower(frase)