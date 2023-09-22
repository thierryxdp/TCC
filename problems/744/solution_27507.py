def hashtag(s):
    """ A Função irá receber um texto/palavra(string) e irá retornar a função com o caractere "#" no início, no meio e no final da string. """
    return "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"