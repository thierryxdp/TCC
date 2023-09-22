def retira_pontuacao(frase):
    '''Esta função, dada uma frase, retorna a mesma frase
    sem caracteres de pontuação
    str -> str'''


    pontuacao_1=str.replace(frase,'/',' ')
    pontuacao_2=str.replace(frase,',',' ')
    pontuacao_3=str.replace(frase,':',' ')
    pontuacao_4=str.replace(frase,';',' ')
    pontuacao_5=str.replace(frase,'.',' ')

    sem_pontuacao= pontuacao_1+pontuacao_2+pontuacao_3+pontuacao_4+pontuacao_5
    
    
    return sem_pontuacao