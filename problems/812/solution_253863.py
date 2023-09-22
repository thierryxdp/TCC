def retira_pontuacao(frase):
    ''' Recebe uma frase e retorna-a substituindo todos os caracteres de pontuação por espaços vazios;
    str => str'''
    return str.replace(str.replace(str.replace(str.replace(frase,'.',' '),'!',' '),',',' '),'?',' ')