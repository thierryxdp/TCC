def retira_pontuacao(frase):
    '''Funcao que, dada uma frase, retorna a mesma frase com
    todos os seus caracteres de pontuacao substituidos por 
    espaço, ou seja, retira todos os caracteres de pontuacao.
    Os caracteres levados em consideracao são travessao, 
    virgula, dois pontos, ponto e virgula, ponto final, 
    reticencias, ponto de interrogacao e ponto de exclamacao.
    str -> str'''
    frase = str.replace(frase,'...', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, ';', ' ')
    return frase

def inverte(frase):
    #antes de iniciar a funcao utilizar a anterior
    '''Função que recebe de entrada uma frase e retorna uma 
    outra frase com as mesmas palavras da frase de entrada 
    em ordem inversa, sem letras maiúsculas e sem pontuacao.
    str -> str'''
    frase = retira_pontuacao(frase) #retirando todas as pontuacoes
    frase = str.lower(frase) #transforma maiusculas em minusculas
    frase = str.split(frase) #aqui foi criada uma lista com as palavras da frase
    list.reverse(frase) #aqui, a ordem dos elementos já foi invertida
    frase = str.join(' ', frase) #aqui, a lista volta a ser string
    return frase #string com as palavras invertidas sem pontuacao e sem maiusculas


#Casos de teste

#inverte('Comi banana, mamao e morango. Estavam deliciosas') ==
# 'deliciosas estavam morango e mamao banana comi'
#inverte('calculo e uma materia que demanda muito tempo e atencao') ==
# ' atencao e tempo muito demanda que materia uma e calculo