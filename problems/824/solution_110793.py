def uppCons (frase: str) -> str:
    """Função que recebe uma frase e retorna uma frase com
    todas as suas consoantes em maiúsculas, e os demais 
    caracteres são mantidos os mesmos."""
    i = 0
    novafrase = ""
    while i < len(frase):
        if frase[i] in "bcdfghjklmnpqrstçvwxyz":
       		novafrase = novafrase + str.upper(frase[i])
        else:
            novafrase = novafrase + frase[i]
        i = i+1
    return novafrase