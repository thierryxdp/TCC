def retira_pontuacao(frase):
    #str -> str
    #Função que retira qualquer tipo de pontuação da frase
    
    pto_final = frase.replace('.', ' ')
    interrogacao = pto_final.replace('?', ' ')
    exclamacao = interrogacao.replace('!', ' ')
    travessao = exclamacao.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    dois_ptos = virgula.replace(':', ' ')
    pto_virgula = dois_ptos.replace(';', ' ')
    
    return pto_virgula