def uppCons(frase):
    """A função recebe uma frase e retorna a mesma frase com todas as consoantes em maiúsculo;
    str->str"""
    frase=str.upper(frase)
    frase=str.replace(frase[1:],"A","a")
    frase=str.replace(frase[1:],"E","e")
    frase=str.replace(frase[1:],"I","i")
    frase=str.replace(frase[1:],"O","o")
    frase=str.replace(frase[1:],"U","u")
    return frase