def hashtag(s):
    """ Função que recebe uma string e insere o caractere # no
    início, meio e final da string.
    str-> str"""
    
    from math import floor
    
    comp_strig = len(s)
    meio_string_par = len(s)-1
    meio_strin_impar = floor(len(s))-1
    
    if comp_string%2 == o:
        return '#' + s[:meio_string_par] + '#' + s[meio_string_par:] + '#'
    else:
        return '#' + s[:meio_strin_impar] + "#" + [meio_strin_impar:] + '#'