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
    minuscula = str.lower(palavras)
    lista1 = str.split(minuscula,' ')
    lista2 = lista1[::-1]
    resultado = " ".join(lista2)
    solucao = str,strip(resultado," ")
    return solucao