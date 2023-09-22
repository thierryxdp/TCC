def lingua_p(string):
    palavra = ""
    vogais="aeiouáéíóúãõ"
    for i in string:
        if i in vogais:
            palavra = palavra +(i + "p" +i)
        else:
                palavra += i
                
    return str.lower(palavra)