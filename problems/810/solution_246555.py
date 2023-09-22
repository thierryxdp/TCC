def retira_pontuacao(frase):
    frase1=str.replace(frase,'.',' ')
    frase2=str.replace(frase1,'-',' ')
    frase3=str.replace(frase2,',',' ')
    frase4=str.replace(frase3,':',' ')
    frase5=str.replace(frase4,'!',' ')
    frase6=str.replace(frase5,'?',' ')
    return frase6

def inverte(frase):
    'inverte uma frase str --> str'
    frase_sempontuacao=retira_pontuacao(frase)
    listafrase=str.split(frase_sempontuacao)
    listareversa=list.reverse(listafrase)
    return str.join(' ',listareversa)