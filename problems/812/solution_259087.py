def retira_pontuacao(s):
    '''Essa função recebe uma string 's' e retorna outra string 's1', sendo essa a 's' sem os delimitadores
    de pontuação'''
    s = s + " "
    s1 = (str.replace(s,". "," "))+(str.replace(s,"? "," "))+(str.replace(s,"! "," "))+(str.replace(s,", "," "))+(str.replace(s,": "," "))+(str.replace(s,"; "," "))+(str.replace(s,"| "," "))