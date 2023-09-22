def filtra_pares(tupla):
    #Criar uma função que receba quatro números inteiros que 
    #sejam tupla e assim retornar um outra tupla com apenas números
    #pares da tupla estabelecida no parâmetro.
    #int, int, int, int -> int
    tupla[0]%2, tupla[1]%2, tupla[2]%2, tupla[3]%2
    if tupla[0]%2==0:
        tupla=tupla[0]
        if tupla[1]%2==0:
            tupla=tupla + tupla[1]
            if tupla[2]%2==0:
                tupla=tupla + tupla[2]
                if tupla[3]%2==0:
                    tupla=tupla + tupla[3]
                    return tupla