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