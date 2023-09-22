def hashtag(str):
    """ Função que recebe uma string e coloca o caractere # no início
    no meio e no final da string.
    str-> str"""
    from math import floor
    comprimento_string = len(str)
    meio_string_par = len(str)/2 - 1
    meio_string_impar= floor(len(str)/2)-1
    if comprimento_string%2 == 0:
        return # + str[:meio_string_par] + # + str[meio_string_par:] + #
    else:
        return # + str[:meio_string_impar] + # + str[meio_string_impar:] + #