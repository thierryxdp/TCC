'Função que dado uma string, retorna uma string como caracter # no início, meio e fim da mesma'
# str-> str
def hashtag(s):
     return s['#', [1::2] , '#' , [-1] , '#']