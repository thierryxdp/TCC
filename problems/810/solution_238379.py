def inverte(frase):
    frasef = str.split(frase, ' ')
    frasef = str.join('', frase[0:-1])
    frasef = str.replace(str.replace(str.replace(str.replace(str.replace(frase, ',', ' '), '!',' '),'.',' '), '?', ' '),'-', ' ')
    return frasef