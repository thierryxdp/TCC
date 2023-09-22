lingua_p(palavra):
    newpalavra:''
    vogais:['a','e','i','o','u','A','E','I','O','U']
        for n in palavra:
            if n in vogais:
                newpalavra=palavra[n:]+'p'+palavra[:n+1]
        return newpalavra