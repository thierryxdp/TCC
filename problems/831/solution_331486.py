def lingua_p(palavra):
    vogais=["a","e","i","o","u","á","ú","í","é"]
    i=0
    while i < len(vogais):
        palavra = str.replace(palavra,vogais[i],vogais[i]+"p"+vogais[i])
    	i = i + 1
    return palavra