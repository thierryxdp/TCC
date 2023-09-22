# Insere o caracetere hashtag no inicio, meio e fim da função
# str-> str
import math

def meio(s):
    return math.ceil(len(s)/2)

def hashtag(s):
    return str('#') + s[0:meio(s)] + str('#') + s[meio(s):] + str('#')