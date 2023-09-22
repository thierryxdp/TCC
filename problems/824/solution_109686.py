def uppCons(frase):
    """Função que recebe como entrada uma frase e retorna a frase com 
       todas as suas consoantes em maiúscula e os demais caracteres 
       exatamente como estavam na frase original.
       str->str
       
       Parâmetros:
       frase: A frase que será passada para a função.
       
       Returns: A frase com todas as suas consoantes em maiúscula e os 
                demais caracteres exatamente como estavam na frase 
                original.
    """
    contador = 0
    novafrase = ""
    while contador < len(frase):
        if frase[contador] in ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','ç'):
            novafrase += str.upper(frase[contador])
        else:
            novafrase += frase[contador]
        contador = contador + 1
    return str(novafrase)