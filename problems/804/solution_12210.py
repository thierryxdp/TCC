def filtra_pares(a,b,c,d):
    "recebe 4 elementros inteiros e calcula uma nova tupla contendo apenas elementos pares"
    "int,int,int,int->int,int,int,int"
    tupla=()
    if (a%2)==0:
        tupla= tupla +(a,)
    if (b%2)==0:
        tupla= tupla +(b,)
    if (c%2)==0:
        tupla= tupla +(c,)
    if (d%2)==0:
        tupla= tupla +(d,)
    return tupla