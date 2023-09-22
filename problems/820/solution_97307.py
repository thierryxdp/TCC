def posLetra(frase: str, letra, numero: int) -> int:
    i = 0
    total = ()
    if str.count(frase, letra) == 0:
        return '-1'