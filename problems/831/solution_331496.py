def lingua_p(palavra):
    """funcao que retorna a palavra traduzida em lingua p, ou seja, retorna a palavra original, mas com a adicao de p apos uma vogal e a propria;
    str -> str"""
    palavra_traduzida=""
    for letra in palavra:
        if letra in "AEIOUaeiouÁÉÍÓÚáéíóúãõ":
            palavra_traduzida=palavra_traduzida+letra+'p'+letra
        if letra not in "AEIOUaeiouÁÉÍÓÚáéíóúãõ":
            palavra_traduzida=palavra_traduzida+letra
    return palavra_traduzida