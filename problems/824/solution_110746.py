def uppCons (frase: str) -> str:
    """Função que recebe uma frase e retorna uma frase com
    todas as suas consoantes em maiúsculas, e os demais 
    caracteres são mantidos os mesmos."""
    i = 0
    while i < len(frase):
        if frase[i] in "AEIOUaeiou":
            frase[i:i] = str.upper(frase[i])
        i = i+1
  return frase