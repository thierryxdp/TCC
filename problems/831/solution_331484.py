def lingua_p(palavra):
    vogais=["a","e","i","o","u"]
    i=0
    while i < 5:
        palavra = str.replace(palavra,vogais[i],vogais[i]+"p"+vogais[i])
    	i = i + 1
    return palavra