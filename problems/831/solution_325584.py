def lingua_p(palavra):
2	    """ Dado uma palavra, a função retorna a a palavra traduzida na língua do p, ex: entao-> epentapaopo;
3	    str->str"""
4	    palavra=str.lower(palavra)
5	    palavra1=palavra[:]
6	    vogais=['a','e','i','o','u']
7	    for i in range(len(palavra)):
8	        if palavra[i] in vogais:
9	            list.remove(vogais,palavra[i])
10	            palavra1=str.replace(palavra1,palavra[i],palavra[i]+'p'+palavra[i])
11	    return palavra1