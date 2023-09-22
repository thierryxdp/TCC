def hashtag(s):
    """Recebe uma string e adiciona o caractere "#" no meio, no inicio e no final dela
    str -> str"""
    return "#" + s[:len(s) // 2] + "#" + s[len(s) // 2:] + "#"