"""def posLetra(s, l, n):
	ct = 0
	i = 0
	while i < len(s):
		if (s[i] == l):
			ct += 1
		if (ct == n):
			return i
        i += 1
    if (n > ct):
        return -1"""
def posLetra(string,letra,ocr):
    """Recebe uma string, uma letra e um número que indica a ocorrência desejada da letra;
    str, str, int -> int"""
    x = 0
    tamanho = len(string)
    y = 1
    while x < tamanho:
        if string[x] == letra:
            if y == ocr:
                return x
            else:
                y = y+1
        x = x+1
    return -1