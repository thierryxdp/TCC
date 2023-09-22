def hashtag(str):
    """Recebe uma string e insere o caracte # no início, meio e fim
    dela.
    Entrada: string
    Saída: string
    """
    from math import floor
    
    x=len(str)
    meio_string_par = x/2-1
    meio_string_impar = floor(x/2)-1
    
    if x%2 == 0:
        return '#'+str[:meio_string_par] + '#' + str[meio_string_par] + '#'
    else:
        return '#' + str[:meio_string_impar] + '#' + str[meio_string_impar:] + '#'