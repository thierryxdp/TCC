def retira_pontuacao(txt):
    '''Dada uma frase txt, retorna a frase onde todos os 
    caracteres de pontuação (incluindo travessão, vírgula, 
    dois pontos, ponto e vírgula, além da pontuação de 
    encerramento de frase) tenham sido substituídos por 
    espaço
    str -> str'''
    pontos = '-,:;.!?'
    for ponto in pontos:
        txt = txt.replace(ponto,' ')
    return