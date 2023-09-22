def substitui(s, x, i):
    '''
        Função responsável por substituir um caractere em uma string de acordo com a posição selecionada.
        s: String
        x: Caractere que vai substituir
        i: Posição onde será substituído o caractere
        Saída: Str, Str, Int  => Str
    '''
    s = list(s)
    s[i] = x
    s = ''.join(s)
    return s