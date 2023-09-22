def retira_pontuacao(frase):
    ''' Função que dada uma string (frase) que represente uma
    frase qualquer, retorna uma frase que no lugar dos caracteres
    de pontuação retorna espaço.
    Entrada: str
    Retorno: str '''

    sem_caracteres = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,"...","."),"."," "),"?"," "),"!"," "),"-"," "),","," "),":"," "),";"," ")

    return sem_caracteres