# Esta função serve para juntar strings no formato abba
# str, str -> str
def concatenacao(a, b):
    return a + b + b + a
	"Faz a junção das strings no formato abba"

#casos de teste:
"""
concatenacao("salve","familia") == 'salvefamiliafamiliasalve'
concatenacao("1","2") == '1221'
concatenacao("1","familia") == '1familiafamilia1'
"""