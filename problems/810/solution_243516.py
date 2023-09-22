def retira_pontuacao(frase):
    """função que transforma as pontuações em espaço"""
    frase1=str.replace(frase,'-', ' ')
    frase2=str.replace(frase1,',',' ')
    frase3=str.replace(frase2,':',' ')
    frase4=str.replace(frase3,'...',' ')
    frase5=str.replace(frase4,';',' ')
    frase6=str.replace(frase5,'?',' ')
    frase7=str.replace(frase6,'!',' ')
    frase8=str.replace(frase7,'.',' ')
    return frase8
def inverte(frase):
    """função que inverte a frase sem maiuscula e sem pontuação
    str->str"""
	frasex=retira_pontuacao(frase)
    frasey=str.lower(frasex)
    frasez=str.split(frasey,' ')
    frasew=list.reverse(frasez)
    separator=' '
	array=[frasew]
    return ([separator.join(array)][0])