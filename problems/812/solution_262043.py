def retira_pontuacao(texto):
    ''' funcao que recebe uma frase e transforma seus caracteres de pontuacao em espaco '''
    for caractere in "!@#$%¨*,.?/": 
    texto = texto.replace(caractere," ")
    return texto