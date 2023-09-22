def hashtag(string):
    'Dada uma string, retorna a string com # no início, meio e fim. Entrada: str. Saída: str'
    meio=(len(string))//2
    caractere='#'
    return caractere+string[0:(meio-1)]+caractere+string[(meio):]