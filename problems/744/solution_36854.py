def hashtag(s):
    """Função que recebe uma string s como entrada e insere o
    caractere "#" no ínicio, no meio e no final da string;
    string -> string"""

    stringEntrada= str(s)
    comprimento= len(s)
    razao= comprimento//2
    stringHashTag= '#' + stringEntrada[:razao] + '#' + stringEntrada[razao:] + '#'
    return stringHashTag