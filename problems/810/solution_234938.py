def retira_pontuacao(s):
    ''' Função que, a partir de uma frase, retorna a frase sem os sinais de pontuação, que são substituidos por espaços; string->string''' 
    tiraponto= str.replace(s,'.',' ')
    tiravirgula= str.replace(tiraponto,',',' ')
    tira_ex= str.replace(tiravirgula,'!',' ')
    tira_in= str.replace(tira_ex,'?',' ')
    tira_doisp= str.replace(tira_in,':',' ')
    tira_pev= str.replace(tira_doisp,';',' ')
    tira_tr=str.replace(tira_pev,'-',' ')
    tira_tresp=str.replace(tira_tr,'...',' ')
    tira_tudo= tira_tresp
    return tira_tudo
def inverte(s):
    s1=retira(s)
    s2=str.split(s1,' ')
    s4=s2[-1:0:-1]
    s5= str.join(' ',s4)
    s6= str.lower(s5+' '+s2[0])
    return s6