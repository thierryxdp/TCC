def uppCons(frase):
    """A função recebe uma frase e retorna a mesma frase com todas as consoantes em maiúsculo;
    str->str"""
    frase1=frase[:]
    frase1=str.upper(frase1)
    frase1=str.replace(frase1[1:],"A","a")
    frase1=str.replace(frase1[1:],"E","e")
    frase1=str.replace(frase1[1:],"I","i")
    frase1=str.replace(frase1[1:],"O","o")
    frase1=str.replace(frase1[1:],"U","u")
    return frase[0]+frase1