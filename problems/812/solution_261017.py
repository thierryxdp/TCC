def retira_pontuacao(frase):
    '''funcao que recebe uma frase, retira todos os caracteres de pontuacao presentes na mesma e retorna essa frase com as pontuacoes sendo substituidas por espaço
    str -> str'''
    pontuacao=('-',',',':',';','.')
    if pontuacao==pontuacao[0]:
        return str.split(frase,pontuacao)