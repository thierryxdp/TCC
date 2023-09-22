def posLetra(frase,letra,numero):
    "função que recebe uma string,uma letra e um número,e retorna em que posição da string a ocorrência da letra está.string,string,int->int."
    indice=0
    numerorepetido = 0
    
    while indice < len(frase):
        if frase[indice] == letra:
            numerorepetido = numerorepetido +1
            if numero == numerorepetido:
                return indice
        indice = indice+1
         return -1