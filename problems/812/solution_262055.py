def retira_pontuacao(texto):
    ''' funcao que recebe uma frase e transforma seus caracteres de pontuacao em espaco 
    str -> str '''
    palavra = str.replace(frase,'?', ' ')
    palavra = str.replace(palavra,'.', ' ')
    palavra = str.replace(palavra,',', ' ')
    palavra = str.replace(palavra,'!', ' ')
    palavra = str.replace(palavra,'-', ' ')
    return palavra