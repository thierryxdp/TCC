def inverte(frase):
    d=frase.split()
    e=d.lower()
    f=e(-1:)
    def retira_pontuacao(frase):
        x=f.replace('.',' ')
        y=x.replace('!',' ')
        w=y.replace('?',' ')
        z=w.replace('-',' ')
        a=z.replace(',',' ')
        b=a.replace(':',' ')
        c=b.replace(';',' ')
        if '.'or'!'or'?'or'-'or','or':'or';'in texto:
            return c