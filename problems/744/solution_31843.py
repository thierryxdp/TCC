'Função que dado uma string, retorna uma string como caracter # no início, meio e fim da mesma'
# str-> str
def hashtag(s):
    string = '#'
    return string[0] , string[1::2] , string [:]