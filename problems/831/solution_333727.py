def lingua_p(x):
    vogal = ('a','e','i','o','u')
    letra = 'p'
    for n in x:
        if n in vogal:
            letra = n + letra + n  
    	print(letra)