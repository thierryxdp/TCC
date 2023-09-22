def retira_pontuacao(frase):
    '''Dada uma frase, retorna a frase onde todos os caracteres de pontuação foram susbstituídos por espaço
    str->str'''
    
    ponto=str.replace(frase,'.',' ',(str.count(frase,'.',)))
    exclamacao=str.replace(ponto,'!',' ',(str.count(ponto,'!',)))
    interrogacao=str.replace(exclamacao,'?',' ',(str.count(exclamacao,'?',)))
    ponto_3=str.replace(interrogacao,'...',' ',(str.count(interrogacao,'...',)))
    travessao=str.replace(ponto_3,'-',' ',(str.count(ponto_3,'-',)))
    virgula=str.replace(travessao,',',' ',(str.travessao(travessao,',',)))
    dois_ponto=str.replace(virgula,':',' ',(str.count(virgula,':',)))
    ponto_virgula=str.replace(dois_ponto,';',' ',(str.count(dois_ponto,';',)))
    
    sem_nada=ponto_virgula

    return sem_nada