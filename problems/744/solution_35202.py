'''Essa função retorna uma string separada por hashtags, str-> str'''
def hashtag(s):
 return '#'+(str(s)[0:1:2])+'#'+(str(s)[2:])+'#'