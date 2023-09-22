def lingua_p(string):
    '''funcao que retorna a palavra dada como entrada traduzida para a lingua do P
    str->str'''
    i=0
    while i<len(string):
        if string[i] in 'aeiouAEIOU':
            string=str.replace(string,string[i],string[i]+'p')
        i=i+1
    return string