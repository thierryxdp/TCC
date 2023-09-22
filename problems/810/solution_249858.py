def inverte(texto):
    ''' funçao que dada uma frase, retorna outra frase com as mesmas
    palavras na ordem inversa, sem letras maiusculas e sem a pontuaçao
    str->str
    '''
    trav=str.replace(texto,'-',' ')
    virg=str.replace(trav,',',' ')
    dois=str.replace(virg,':',' ')
    p_vir=str.replace(dois,';',' ')
    final=str.replace(p_vir,'.',' ')
    excla=str.replace(final,'!',' ')
    inter=str.replace(excla,'?',' ')
    
    mini=str.lower(inter)
    lista=list(str.split(mini))
    reverse= list.reverse(lista)
    #juntar=str.join(',', reverse)
    return reverse