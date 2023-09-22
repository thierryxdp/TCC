def inverte(texto):
    texto = texto.lower()
    #Retirar pontuação
    sem_pont = texto
    sem_pont = sem_pont.replace("...","")
    sem_pont = sem_pont.replace(".","")
    sem_pont = sem_pont.replace(",","")
    sem_pont = sem_pont.replace("?","")
    sem_pont = sem_pont.replace("!","")
    sem_pont = sem_pont.replace("-","")
    sem_pont = sem_pont.replace(";","")
    sem_pont = " " + sem_pont[0] + sem_pont[1::]
    #Separar cada palavra
    lista_palavra = str.split(sem_pont," ")
    #Reverter a lista formada
    lista_final = lista_palavra.reverse()
    #Resultado
    frase_final = str.join(" ",lista_palavra)
    return frase_final