def substitui(s, x, i):
    """
    Subtitui o iésimo caracter de uma string 's' por outro caractere 'x'.
    str, str , int -> str

    Parameters:
    s: Parâmetro textual s, do tipo string (str);
    x: Parâmetro textual x, do tipo string (str);
    i: Parâmetro numérico i, do tipo inteiro (int).
    
    Returns:
    A string com o caracter substituído na posição i.
    """
    
    tamanho = len(s)
    if i >= 0 and i <= tamanho:
        palavra = s.replace(s[i], x)
        return (palavra)
    else:
        return ("Insira um valor entre 0 e ", tamanho)