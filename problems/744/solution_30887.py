def hashtag(s):
    "Função que dade uma string, retorna uma caractere '#'no início meio e fim dela. string--> string ex:'#guil#herme#'" 
    media = len(s) //2
    return "#" + s[0:media] + "#" + s[media:] + "#"