def retira_pontuacao(txt):
    """Dada uma frase, retorna a mesma porém com todos os caractéres substituidos por um espaço. str->str"""
    a = ['-',',',':',';','.','!','?']
    txt = txt.replace(a[0],' ')
    txt = txt.replace(a[1],' ')
    txt = txt.replace(a[2],' ')
    txt = txt.replace(a[3],' ')
    txt = txt.replace(a[4],' ')
    txt = txt.replace(a[5],' ')
    txt = txt.replace(a[6],' ')
    return txt