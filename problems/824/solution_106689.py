def uppCons(frase):
    """A função recebe uma frase e retorna a mesma frase com todas as consoantes em maiúsculo;
    str->str"""
    str.upper(frase)
    str.replace(frase[1:],"A","a")
    str.replace(frase[1:],"E","e")
    str.replace(frase[1:],"I","i")
    str.replace(frase[1:],"O","o")
    str.replace(frase[1:],"U","u")
    return frase