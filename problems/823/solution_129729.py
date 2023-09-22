def faltante(lista_faltante):
    """Dado uma lista contendo n-1 números inteiros positivos, 
    numerada de 1 até n, retorna o úmero inteiro neste intervalo que
    está faltando. Exemplo:
    Entrada:[1,2,4]
    Saída:3
    lista(int)->int"""
    lista_completa=list(range(1,len(lista_faltante)+2))
    i=0
    lista_faltante.sort()
    lista_faltante.append("")
    while i<len(lista_completa):
        i+=1
        if lista_faltante[0]==2:
            return 1
        if lista_completa[i]!=lista_faltante[i]:
            return lista_completa.pop(i)