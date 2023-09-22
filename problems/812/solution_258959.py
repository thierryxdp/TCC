def retira_pontuacao(txt):
    a = ['-',',',':',';','.']
    txt = txt.replace(a[0],' ')
    txt = txt.replace(a[1],' ')
    txt = txt.replace(a[2],' ')
    txt = txt.replace(a[3],' ')
    txt = txt.replace(a[4],' ')
    return txt