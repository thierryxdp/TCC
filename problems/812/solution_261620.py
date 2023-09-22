def retira_pontuacao(frase):
    ''' Função que recebe uma string "frase" de entrada,
    e retorna a mesma string substituindo os caracteres especiais
    ("-", "," , ":", ";", ".","?","!") por um espaço'''
    '''str -> str'''
    #casos de teste:
    ''' retira_pontuacao('Eu-estou, demorando a terminar: meu deus.')
    -> 'Eu estou  demorando a terminar  meu deus '
        retira_pontuacao('provas; provas; preciso estudar mais.')
    -> 'provas  provas  preciso estudar mais '
        retira_pontuacao('ele disse -quimica é facil, brincou.')
    -> 'ele disse  quimica é facil  brincou ' '''
    f1 = str.replace(frase,"?"," ")
    f2 = str.replace(f1,"."," ")
    f3 = str.replace(f2,"!"," ")
    f4 = str.replace(f3,":"," ")
    f5 = str.replace(f4,";"," ")
    f6 = str.replace(f5,"-"," ")
    f7 = str.replace(f6,","," ")
    return f7