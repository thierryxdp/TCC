def inverte(frase):
    """Dada uma frase, a função irá retirar todas as pontuações e só irá deixar acentos e palavras,
    também irá inverter a ordem da frase e substituirá qualquer maiúscula por minúscula.
    Recebe valores do tipo string e retorna um valor do tipo string."""
    frase = frase
    for n in [".", "!", ":", ";", "-", ",", "?"]:
        frase = frase.replace(n, " ")
    frase = frase.lower()
    nova_frase = frase.split()
	nova_frase2 = nova_frase[::-1]
    nova_frase3 = " ".join(nova_frase2)
    return nova_frase3