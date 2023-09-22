def lingua_p(palavra):
    vogais=["a","e","i","o","u"]
    for i in vogais:
        palavra = str.replace(palavra,vogais[i],vogais[i]+"p"+vogais[i])
        return palavra