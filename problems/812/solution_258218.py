def retira_pontuacao(frase):
    '''Esta função, dada uma frase, retorna a mesma frase
    sem caracteres de pontuação
    str -> str'''


    pontuacao_1=str.replace(frase,'/',' ')
    pontuacao_2=str.replace(pontuacao_1,',',' ')
    pontuacao_3=str.replace(pontuacao_2,':',' ')
    pontuacao_4=str.replace(pontuacao_3,';',' ')
    pontuacao_5=str.replace(pontuacao_4,'.',' ')

    
    
    return pontuacao_5