def lingua_p(palavra):
    """Função que recebe uma palavra e a transcreve para a lingua do P
    str -> str"""
    string =''
    for i in palavra:
        if palavra(i) == 'aeiou':
            string = string + palavra[i] + 'p' + palavra[i]
        else:
            string = string + palavra[i]
        i+=1
        return string