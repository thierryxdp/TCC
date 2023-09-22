vogal = 'aeiou'
comeco = 0
str.lower(string)

def lingua_p(string):
    for letra in list(string):
        if letra in vogal:
            palavra = string[0:str.find(string,letra,comeco)] + letra + 'p' + string[str.find(string,letra):]
            comeco += str.find(string,letra)
        return palavra