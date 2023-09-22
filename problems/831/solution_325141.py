def lingua_p(string):
    '''funcao que retorna a palavra dada como entrada traduzida para a lingua do P
    str->str'''
    vogais = ['a','e','i','o','u','A','E','I','O','U']
    for i in string:
        if i in vogais:
            vogal= i+'p'+i
            string = str.replace(string,i,vogal)
    return string