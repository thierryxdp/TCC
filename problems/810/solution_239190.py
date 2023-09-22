#A função recebe uma frase
#1-necessário transformá-la em uma lista, removendo tambem, a pontuação
#2-Inverter a ordem 
#3-voltar a uma string e retornar
def inverte(frase: str)->str:
    #tirando a possível pontuação
    FraseSemPontos=str.replace(str.replace(str.replace(str.replace(str.replace(frase, "-", " "), "!", " "), ","," "), "."," "), "?", " ")
    #Transformando em lista
    listaFrase=str.split(FraseSemPontos)
    #Revertendo a lista
    list.reverse(listaFrase)
    fraseFinal=str.join(" ", listaFrase)
    #retornando
    return fraseFinal.lower()