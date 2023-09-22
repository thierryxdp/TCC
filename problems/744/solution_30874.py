def hashtag(str):
    """Recebe uma string e insere o caracte # no início, meio e fim
    dela.
    Entrada: string
    Saída: string
    """
    antes_do_meio = str[:len(str)//2]
    depois_do_meio = str[len(str)//2:]
    string_final = '#' +  antes_do_meio + '#' +  depois_do_meio + '#'
    return string_final