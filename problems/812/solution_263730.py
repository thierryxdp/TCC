def retira_pontuacao(frase):
    ''' essa função retira todas as pontuações existente na frase, str,str,str'''
    conta = str.join(' ', str.split(frase, '.'))
    cont1 = str.join(' ', str.split(conta, ','))
    return cont1