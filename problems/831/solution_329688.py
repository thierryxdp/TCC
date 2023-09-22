def lingua_p(palavra):
    """recebe uma palavra e retorna essa traduzida para
    a lingua do p (apos cada vogal, adiciona-se o p e
    a propria vogal).
    str -> str"""
    fim=""
    for letra in palavra:
        if letra in "AEIOUaeiouáéíóúâêîôûãõ":
            fim+=(letra+"p"+letra)
        if letra not in "AEIOUaeiouáéíóúâêîôûãõ":
            fim+=letra
    return fim