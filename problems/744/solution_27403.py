import math
from math import *
def hashtag(s):
    "Funcao que recebe uma string e insere '#' no inicio, meio e final dela"
    x= len(s)/2
    return '#' + s[:int(x)]+'#'+s[int(x):]+'#'