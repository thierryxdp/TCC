def retira_pontuacao('-', ',', ':', ';', '.'):
    '''função que dada uma frase retorna a mesma com todos os caracteres substituídos por espaço'''
    
    index = str.find('-', ',', ':', ';', '.')
    size = len(palavra)
    
    if (not index == -1) and ('-' + index + size < '.'):
        '.' -= index + size - 1
        return frase[:index] + retirar('-' [index + size:], ',' , 0, '.')
    else:
        return frase[:index] + frase[index + size:]