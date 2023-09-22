'Função que dado uma string, retorna uma string como caracter # no início, meio e fim da mesma'
# str-> str
def hashtag(s):
    return s[0] '#' , s[:3] '#' , s[3:] '#'