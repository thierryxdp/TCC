def uppCons (frase: str) -> str:
    """Função que recebe uma frase e retorna uma frase com
    todas as suas consoantes em maiúsculas, e os demais 
    caracteres são mantidos os mesmos."""
    i = 0
    novafrase = " "
    while i < len(frase):
        if frase[i] in "bcdfghjklmnpqrstvwxyz":
       		novafrase = str.upper(frase[i])
        i = i+1
        if frase[i] not in  "bcdfghjklmnpqrstvwxyz":
            novafrase = frase[i]
        i = i+1
    return novafrase