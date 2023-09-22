# Insere o caracetere hashtag no inicio, meio e fim da função
# str-> str
def meio(s):
    return round(len(s)/2)

def hashtag(s):
    return str('#') + s[0:meio(s)] + str('#') + s[meio(s):] + str('#')