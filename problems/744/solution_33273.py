def quantidade(s):
    return len(x)
def meio(s):
    return quantidade(s)/2
def hashtag(s):
    """retorne a string de entrada com o formato de #no início, no meio e no final da string"""
    return s[:meio(s)]+"#"+s["#"+1:]