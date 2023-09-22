def inverte(frase):
    '''Função que retorna a frase dada com a frase na ordem inversa e sem letra maiúscula e sem pontuação
       string->string '''

    frase= str.replace(frase,'-',' ')
    frase= str.replace(frase,',',' ')
    frase= str.replace(frase,':',' ')
    frase= str.replace(frase,';',' ')
    frase= str.replace(frase,'.',' ')
    frase= str.replace(frase,'?',' ')
    frase= str.replace(frase,'!',' ')
    frase= str.lower(frase)
    frase= str.split(frase)
    list.reverse(frase)
    frase=str.join(' ',frase)
    return frase