def hashtag(s):
    """ Função que recebe uma string e insere o caractere # no
    início, meio e final da string.
    str-> str"""
    
    from math import floor
    
    comp_string = len(s)
    meio_string_par = len(s)/2-1
    meio_strin_impar = floor(len(s)/2)-1
    
    if comp_string%2 == 0:
        return '#' + s[:meio_string_par] + '#' + s[meio_string_par:] + '#'
    else:
        return '#' + s[:meio_strin_impar] + "#" + s[meio_strin_impar:] + '#'