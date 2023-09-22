''' Essa função retorna uma string separada por hastags #
str-> str'''
def hashtag(s):
    return '#'+(str(s)[0:3])+'#'+(str(s)[4:])