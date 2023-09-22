def retira_pontuacao(frase):
    "Função que substitui toda a pontuação da frase por espaços. str --> str"
    NewF=str.replace(frase,'.',' ')
    NewF=str.replace(NewF,',',' ')
    NewF=str.replace(NewF,';',' ')
    NewF=str.replace(NewF,':',' ')
    NewF=str.replace(NewF,'-',' ')
    NewF=str.replace(NewF,'!',' ')
    NewF=str.replace(NewF,'?',' ')
    NewF=str.replace(NewF,'...',' ')
    return NewF

def inverte(frase):
    "Função que retorna, uma dada string de entrada, sem pontuação, letras maiusculas e com as palavras em ordem inversa. str --> str"
    frase= str.lower(frase)
    frase= retira_pontuacao(frase)
    lista= str.split(frase)
    lista.reverse()
    invertido= str.join(" ", lista)
    return invertido