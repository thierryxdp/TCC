vogal = 'aeiou'

def lingua_p(string):
    
    comeco = 0
    str.lower(string)
    palavra=string
    
    for letra in list(string):
        if letra in vogal:
            palavra = palavra[0:str.find(palavra,letra,comeco)] + letra + 'p' + string[str.find(palavra,letra):]
            comeco += str.find(palavra,letra)
            
    return palavra