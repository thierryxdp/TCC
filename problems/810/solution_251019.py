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
    list.reverse(frase)
    frase = str.join('',frase)
    return str.lower(frase)