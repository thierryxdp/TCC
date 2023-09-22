def substitui(s, x, i):
    """Função que retorna uma nova string dado uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da string. str->str."""
    if i <= len(s):
        return  s[:i] + x + s[i+1:]