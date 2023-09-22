def posLetra(frase: str, letra, numero: int) -> int:
    i = 0
    total = ()
    while i < len(frase):
        if frase[i] == letra:
            total = total + 1
    return int(total) / numero