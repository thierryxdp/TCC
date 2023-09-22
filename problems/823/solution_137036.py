def faltante(lista_numeros):
    "função que retorna o número está faltando num intervalo de números"
    "list -> int"
    list.sort(lista_numeros)
    i=len(lista_numeros)
    lista_correta=list(range(1,i+2))
    lista_faltantes=[]
    x=0
    while x+1<len(lista_correta):
        if lista_numeros[x]!=lista_correta[x]:
            return lista_correta[x]
        x=x+1
    return lista_correta[-1]