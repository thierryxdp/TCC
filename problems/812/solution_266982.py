def retira_pontuacao(frase):
    '''função que recebe uma frase e retorna a mesma com 
    todos os sinais de pontuação se transformaram em espaços'''
    f=frase
    f=str.replace(f,"!"," ")
    f=str.replace(f,"."," ")
    f=str.replace(f,"?"," ")
    f=str.replace(f,","," ")
    f=str.replace(f,"-"," ")
    return f