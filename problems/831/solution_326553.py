def lingua_p (palavra):
    """funçao que recebe uma palavra em portugues e retorna a mesma palavra traduzida na lingua do P;
entrada: str;
saida: str."""

    palavra = str.lower (palavra)
    P = ''

    for i in range (len (palavra)):
        if i == 'aeiou':
            P = P + ipi
    return P