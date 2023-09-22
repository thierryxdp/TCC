def lingua_p(string):
    '''funcao que retorna a palavra dada como entrada traduzida para a lingua do P
    str->str'''
    i=0
    novastring=()
    for letra in string:
        if string[i] in 'aeiouAEIOU':
            copia=string
            novastring=str.replace(copia,copia[i],copia[i]+'p'+copia[i])
    return novastring