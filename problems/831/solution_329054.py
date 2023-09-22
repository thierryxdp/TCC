def lingua_p(palavra):
    """funcao que recebe uma palavra e a retorna traduzida para a lingua do p, onde apos cada vogal é adicionado o conjunto formado pelo p mais a vogal original;
       str->str"""
    palavra_trad=""
    for letra in palavra:
        if letra not in "qwrtypsdfghjklzxcvbnm":
            palavra_trad=palavra_trad+letra+"p"+letra
        else:
            palavra_trad=palavra_trad+letra
    return palavra_trad