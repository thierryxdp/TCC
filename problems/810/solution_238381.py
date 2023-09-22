def inverte(frase):
    frasef = str.split(frase, ' ')
    frasef = str.join('', frase[-1:0:-1])
    frasef = str.replace(str.replace(str.replace(str.replace(str.replace(frase, ',', ' '), '!',' '),'.',' '), '?', ' '),'-', ' ')
    return frasef