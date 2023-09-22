def retira_pontuacao(frase):
    '''funcao que dado uma frase retorna sem nehuma pontuacao;
    str -> str'''
    retira1 = str.strip(frase,'.')
    retira2 = str.strip(retira1,'-')
    retira3 = str.strip(retira2,',')
    retira4 = str.strip(retira3,';')
    retira5 = str.strip(retira4,':')
    retira6 = str.strip(retira5,'?')
    retira7 = str.strip(retira6,'!')
    frase_final = retira7
    
    return frase_final