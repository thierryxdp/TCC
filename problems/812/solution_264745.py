def retira_pontuacao(frase):
    '''Função que, dada uma frase, retorna
    a frase onde todos os caracteres de pontuação
    (incluindo travessão, vírgula, dois pontos, ponto
    e vírgula, além da pontuação de encerramento da 
    frase) tenham sido substituídos por espaço'''
    if str.find(frase,"-")