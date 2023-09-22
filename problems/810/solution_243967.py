def retira_pontuacao(frase):
    '''calcule uma função que, dada uma frase,retorne a frase com todos os caracteres de pontuação substuídos por espaço.str-->str.'''
    frase_nova = (frase.replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('.',' ').replace('?',' ').replace('!',' '))
    return frase_nova

def inverte(frase1):
    '''calcule uma funcao que, dada uma frase, retorne essa frase na ordem contrária, sem a pontuação e sem letras maiúsculas.str--str.'''
    sem_pontuacao = retira_pontuacao(frase1)
    sem_maiusculas = str.lower(frase1)
    inversao = list.reverse(str.split(frase1))
    return (inversao)+(sem_maiusculas)+(sem_pontuacao)