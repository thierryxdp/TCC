def retira_pontuacao(f):
    "str-->str"
    "Troca todas as pontuações de uuma frase por espaços"
    #essa troca é feita de 1 a 1, retirando um tipo de pontuação de cada vez e adicionando os espaços, tendo no final todos os tipos de pontuação trocados por espaços.
    f1= str.replace(f,"-"," ")
    f2= str.replace(f1,","," ")
    f3= str.replace(f2,":"," ")
    f4= str.replace(f3,";"," ")
    f5= str.replace(f4,"?"," ")
    f6= str.replace(f5,"!"," ")
    f7= str.replace(f6,"."," ")
    return f7