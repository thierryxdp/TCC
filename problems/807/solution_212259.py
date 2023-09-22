def conta_frases(s):
    """calcula e retorna a quantidade de frases presentes em um texto de entrada;
    str, str -> int"""
    if "..." in s:
        str.replace("...","!")
        return str.count(s,"!")+str.count(s,"?")+str.count(".")