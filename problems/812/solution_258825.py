def retira_pontuacao(texto):
    ''' função que retorna um texto tendo todas as suas 
    pontuações substituidas por espaço, dado como entrada o
    texto. str->str'''
    x = str.replace(texto, '-', ' ')
    y = str.replace(x, ',', ' ')
    z= str.replace(y, ':', ' ')
    w= str.replace(z, ';', ' ')
    t_final= str.replace(z, '.', ' ')
    return t_final