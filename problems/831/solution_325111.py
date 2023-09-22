def lingua_p(string):
    '''funcao que retorna a palavra dada como entrada traduzida para a lingua do P
    str->str'''
    i=0
    for letra in range(string):
        if string[i] in 'aeiouAEIOU':
            string=str.replace(string,string[i],string[i]+'p')
    return string