def posLetra(s, let, n):
    """Recebe como parâmetro uma string, uma letra e um número que indica a ocorrência desejada da letra e retorna a posição da string que aquela ocorrência da letra está. Caso exista menos ocorrências da letra do que a ocorrência pedida, retorna -1;
    assinatura: str, str, int --> int
    Casos de teste:
    posLetra('mariana come banana', 'a', 3) == 6
    posLetra('mariana come banana', 'a', 9) == -1
    posLetra('mariana come banana', 'n', 2) == 15"""
    o = 0
    lista_aux = []
    for i, ch in enumerate(s):
        if ch == let:
            o += 1
            lista_aux.append((ch, i, o))
            
    if o < n:
        return -1
    else:
        for e1, e2, e3 in lista_aux:
            if e3 == n:
                return e2