def inverte(frase):
    def retira_pontuacao(frase):
        x=frase.replace('.',' ')
        y=x.replace('!',' ')
        w=y.replace('?',' ')
        z=w.replace('-',' ')
        a=z.replace(',',' ')
        b=a.replace(':',' ')
        c=b.replace(';',' ')
        d=str.split(c,' ')
        e=d.lower()
        f=e[::-1]
        g=' '.join(f)
        return g