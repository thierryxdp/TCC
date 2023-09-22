def repetidos(lista):
    anterior = ""
    contador = 0
    for char in lista:
        if(char == anterior):
            contador +=1
        anterior = char