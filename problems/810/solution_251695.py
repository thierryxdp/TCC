def inverte(frase):

    frase = str.split(frase,'N')
    frase = str.join('n',frase)
    frase = str.split(frase,'A')
    frase = str.join('a',frase)
    frase = str.split(frase,'S')
    frase = str.join('s',frase)
    frase = str.split(frase,'F')
    frase = str.join('f',frase)
    frase = str.split(frase,'T')
    frase = str.join('t',frase)
    frase = str.split(frase,'!')
    frase = str.join(' ',frase)
    frase = str.split(frase,'?')
    frase = str.join(' ',frase)
    frase = str.split(frase,'.')
    frase = str.join(' ',frase)
    frase = str.split(frase,':')
    frase = str.join(' ',frase)
    frase = str.split(frase,'-')
    frase = str.join(' ',frase)
  
    lista = str.split(frase)
    lista.reverse()
   
    frase = str.join(' ', lista)
    return frase