def inverte(frase):
    """..."""
    x = frase
    y = str.lower(x)
    z = list(y)
    a = list.reverse(z)
    b = "-".join(a)
def retira_pontuacao(b):
    if "-" or "," or ":" or ";" or "!" or "?" or "." in b:
         return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(b, "-", ""), ",", ""), ":", ""), ";", ""), "!", ""), "?", ""), ".", "")