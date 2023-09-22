if ((',' in texto)== True):
        t=str.replace(texto,',',' ')
        e=str.split(t)
        x=e[::-1]
        return str.join(' ',x)