#Questão 3
def bolos (a,b,c):
    '''Função que retorna o número máximo de bolos possíveis de serem
       feitos com os ingredientes disponíveis'''
    '''A=xícaras de farinha de trigo, B=ovos e C=colheres de sopa de leite'''
    return min (a//2,b//3,c//5)