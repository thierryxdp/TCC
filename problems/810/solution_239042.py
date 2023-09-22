def retira_pontuacao(frase):
    a=frase.replace("-","")
    b=a.replace(",","")
    c=b.replace(":","")
    d=c.replace(";","")
    e=d.replace(".","")
    f=e.replace("!","")
    g=f.replace("?","")
    return g

def inverte(frase):
    '''funcao que inverte a frase escrita. str->str'''
    a = retira_pontuacao(frase)
    lista=a.split(" ")
    b=lista.reverse()
    return (" ".join([str(_) for _ in lista])).lower()