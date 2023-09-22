def inverte(frase):
    """..."""
    x = frase
    y = list(str.lower(x))
    a = list.reverse(y)
    b = str.join(' ', a)
def retira_pontuacao(b):
    if "-" or "," or ":" or ";" or "!" or "?" or "." in b:
         return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(b, "-", ""), ",", ""), ":", ""), ";", ""), "!", ""), "?", ""), ".", "")