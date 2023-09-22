#Função que coloca uma hashtag no início, meio e fim da ums dada string
# str-> str
import math
def hashtag(string):
    return "#" + string[0:math.floor(len(string))] + "#" + string[math.floor(len(string)):] + "#"