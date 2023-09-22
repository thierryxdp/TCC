def inverte(frase):
    '''retorna a frase sem pontuação, sem letras maiúsculas 
    e em ordem invertida de palavras
    str->str'''
    semunder=str.replace(frase,'_','')
    semvir=str.replace(semunder,',','')
    semdois=str.replace(semvir,':','')
    sempontovir=str.replace(semdois,';','')
    semexcla=str.replace(sempontovir,'!','')
    seminter=str.replace(semexcla,'?','')
    semponto=str.replace(seminter,'.','')
    semhifen=str.replace(semponto,'-','')
    minusculo=str.lower(semhifen)
    palavras=str.split(minusculo,' ')
    return str.strip(str.join(' ',palavras[::-1]))