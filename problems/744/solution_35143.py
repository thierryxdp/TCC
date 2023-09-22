''' Essa função retorna uma string separada por hastags #
str-> str'''
def hashtag(s):
    return '#'+(str(s)[0:5])+'#'+(str(s)[4:])+'#'