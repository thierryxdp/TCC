def inverte(frase):
    tiraponto=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'?',' '),'.',' '),'!',' '),'...',' '),'-',' '),',',' '),':',' '),';',' ')
    return str.lower(str.join(' ',list((str.split(tiraponto))[-1:(len(str.split(tiraponto))*(-1)-1):-1])))