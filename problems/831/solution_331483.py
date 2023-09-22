def lingua_p(palavra):
    vogais=["a","e","i","o","u"]
    i=0
    for i in vogais:
        palavra = str.replace(palavra,vogais[i],vogais[i]+"p"+vogais[i])
    	i = i + 1
    return palavra