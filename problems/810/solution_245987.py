def retira_pontuacao(fraseAlterada):
    """ dado uma frase retorna a mesma com todas as pontuações substituidas por espaço
    str->str"""
    fraseAlterada = fraseAlterada.replace('...',' ')
    fraseAlterada = fraseAlterada.replace('.',' ')
    fraseAlterada = fraseAlterada.replace(',',' ')
    fraseAlterada = fraseAlterada.replace('-',' ')
    fraseAlterada = fraseAlterada.replace(';',' ')
    fraseAlterada = fraseAlterada.replace(':',' ')
    fraseAlterada = fraseAlterada.replace('?',' ')
    fraseAlterada = fraseAlterada.replace('!',' ')
    return fraseAlterada

def inverte(frase:str)->str:
    """dada uma frase retorna a mesma invertida sem pontuação"""
    copia = frase[:]
    palavras = retira_pontuacao(frase)
    lista = str.split(palavras)
    lista1 = list.reverse(lista)
    lista2 = str.join(' ',lista1)
    return lista_2