def retira_pontuacao(ponto):
    '''
    Funcao que, dada uma frase, retorne a frase 
    onde todos os caracteres de pontuação travessão, 
    vírgula, dois pontos, ponto e vírgula, além da 
    pontuação de encerramento de frase) tenham sido 
    substituídos por espaço.
    str -> str
    '''
    for char in '- , : ; . ? !':
        ponto = ponto.replace(char, ' ')
    return ponto

#Questao 4
def inverte(frase):
    '''
    Funcao chamada inverte que dada uma frase retorne 
    uma outra frase que contenha as mesmas palavras da 
    frase de entrada na ordem inversa, sem letras 
    maiusculas, e sem a pontuação
    
    '''
    for char in '- , : ; . ? !':
        ponto = ponto.replace(char, ' ')
    return ponto