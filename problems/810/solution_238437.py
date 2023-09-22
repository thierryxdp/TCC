def inverte(frase):
    """funcao que retorna uma frase invertida sem pontuaçao;str->str"""
    f=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-',' '),',',' '),':',' '),';',' '),'!',' '),'.',' '),'?',' ')
    f=str.split(f)
    list.reverse(f)
    return str.join(' ',f)