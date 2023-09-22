def hashtag(s):
    """ Função que recebe uma string e coloca o caractere # no início
    no meio e no final da string.
    str-> str"""
    from math import floor
    comprimento_string = len(s)
    meio_string_par = len(s)/2 - 1
    meio_string_impar= floor(len(s)/2)-1
    if (comprimento_string%2) = 0:
        return # + s[:meio_string_par] + # + s[meio_string_par:] + #
    else:
        return # + s[:meio_string_impar] + # + s[meio_string_impar:] + #