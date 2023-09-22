def retira_pontuacao(frase):
    '''função que recebe uma frase e troca todos os tipos de pontuação por espaços
str->str'''

    frase=str.replace(frase,'...',' ')     #o nome da variavel tem que ser o mesmo da string pra ele atualizar oq já foi atualizado antes, senão só a última mudança que aconteceria
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')

    return frase