def retira_pontuacao(frase):
    '''função que dada uma frase, retorne a frase onde
    todos os caracteres de pontuação(incluindo travessão,
    virgula, dois pontos, ponto e vírgula, além da pontuação
    de encerramento de frase) tenham sido substituídos por espaço;
    str -> str'''
    finicial=str.replace(frase,'!',' ')
    frase2=str.replace(finicial,'?',' ')
    frase3=str.replace(frase2,'...', ' ')
    frase4=str.replace(frase3,'.',' ')
    frase5=str.replace(frase4,',',' ')
    frase6=str.replace(frase5,';',' ')
    frase7=str.replace(frase6,':',' ')
    ffinal=str.replace(frase7,'-',' ')
    return ffinal

def inverte(frase):
    '''função que dada uma frase retorna uma outra frase que 
     contenha as mesmas palavras da frase de entradada na ordem iversa,
     sem letras maiúsculas, e sem a pontuação; str -> str'''
    frase1= (retira_pontuacao(frase))
    frase2= str.lower(frase1)
    lista= str.split(frase2)
    lista.reverse()
    str= frase[::-1]
    f=str.join('', lista)
    return f