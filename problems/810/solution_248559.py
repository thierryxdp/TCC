def inverte(frase):
    naw=str.replace(frase,'.',' ')
    new=str.replace(naw,'?',' ')
    now=str.replace(new,'!',' ')
    nuw=str.replace(now,'-',' ')
    niw=str.replace(nuw,'...',' ')
    nrw=str.lower(niw)
    ntw=str.split(nrw)
    return reversed(ntw)