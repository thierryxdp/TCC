def substitui(s,x,i):
    """Função que recebe uma string(s), um caractere(x) e um número inteiro(i) entre
    0 e o comprimento da string, e retorna uma string igual a s, exeto que o elemento
    da posição "i" deve ser substituído pelo caractere "x".
    string, string, int -> string"""
    a = s[0:(i)]
    b = s[(i+1):(len(s))]
    
    return (str(a) + str(x) + str(b))