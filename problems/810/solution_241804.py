def inverte(frase):
    """Dada uma frase, a função irá retirar todas as pontuações e só irá deixar acentos e palavras,
    substituindo as pontuações por espaço em branco.
    Recebe valores do tipo string e retorna um valor do tipo string."""
    frase = frase
    for n in [".", "!", ":", ";", "-", ",", "?"]:
        frase = frase.replace(n, " ")
    frase = frase.lower()
    nova_frase = frase.split()
	nova_frase2 = nova_frase[::-1]
    return nova_frase2