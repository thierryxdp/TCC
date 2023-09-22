import math
def hashtag(s):
    #retorna a string com hashtag no inicio, meio e fim dela
    #Divide a string no meio caso seja par, caso nao seja divide no meio - 1 
    # str-> str
    string = list(s)
    string.insert(0, '#')
    string.append('#')
    if len(s)%2 == 0:
        meio = len(string) // 2
    else:
        meio = math.ceil((len(string))/2 - 1)
    string.insert(meio, '#')
    string = "".join(string)
    return string