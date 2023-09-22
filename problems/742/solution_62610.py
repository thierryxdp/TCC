"Dados uma string, um caractere e um número, substitui a letra da palavra no índice desejado pelo"
"caractere escolhido."
"string, string, int -> string"

def substitui(s, x, i):
    novaPalavra = s[ : i] + x + s[i + 1: ]
    return novaPalavra