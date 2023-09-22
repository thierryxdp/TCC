def inverte(frase):
    '''retorna a frase sem pontuação, sem letras maiúsculas 
    e em ordem invertida de palavras
    str->str'''
    semunder=str.strip(str.replace(frase,'_',' '))
    semvir=str.strip(str.replace(semunder,',',' '))
    semdois=str.strip(str.replace(semvir,':',' '))
    sempontovir=str.strip(str.replace(semdois,';',' '))
    semexcla=str.strip(str.replace(sempontovir,'!',' '))
    seminter=str.strip(str.replace(semexcla,'?',' '))
    semponto=str.strip(str.replace(seminter,'.',' '))
    semhifen=str.strip(str.replace(semponto,'-',' '))
    minusculo=str.strip(str.lower(semhifen))
    palavras=str.split(minusculo,' ')
    return str.strip(str.join(' ',palavras[::-1]))