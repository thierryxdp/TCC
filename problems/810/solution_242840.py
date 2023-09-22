'''Nessa questao devemos nos basear na inversao da ordem das palavras 
da frase dada como parametro. Para fazer isso, devemos 
1) separar as palavas dessa lista com o comando str.split 
e isso nos retornara uma lista. 
2) A partir dessa lista, iremos inverter a ordem de seus 
elementos (palavras) com o comando list.reverse. 
3) Com a lista já invertida, precisamos transforma-la 
de volta em uma string, e para isso, usamos o comando 
str.join(' ',frase). esse comando join pode receber 
como 2° parametro uma sequencia de strings dentro de 
uma lista. Não esquecer de transformar tudo em 
minuscula e retirar a pontuacao
'''
def retira_pontuacao(frase):
    '''Funcao que, dada uma frase, retorna a mesma frase com todos os seus caracteres
    de pontuacao substituidos por espaço, ou seja, retira todos os caracteres de pontuacao.
    str -> str'''
    s = frase
    s = str.replace(s,'...', ' ')
    s = str.replace(s, '!', ' ')
    s = str.replace(s, '?', ' ')
    s = str.replace(s, '.', ' ')
    s = str.replace(s, '-', ' ')
    s = str.replace(s, ',', ' ')
    s = str.replace(s, ':', ' ')
    s = str.replace(s, ';', ' ')
    return s

def inverte(frase):
    #antes de iniciar a funcao utilizar a anterior
    '''Função que recebe de entrada uma frase e retorna uma 
    outra frase com as mesmas palavras da string de entrada 
    em ordem inversa, sem letras maiúsculas
    e sem pontuacao.
    str -> str'''
    f = frase
    f = retira_pontuacao(f) #retirando todas as pontuacoes
    f = str.lower(f) #transforma maiusculas em minusculas
    f = str.split(f) #aqui foi criada uma lista com as palavras da frase
    list.reverse(f) #aqui, a ordem dos elementos já foi invertida // não tem como atribuir isso a uma variável, pois seu retorno é Non-Type
    f = str.join(' ', f) #aqui, a lista volta a ser string
    return f #string com as palavras invertidas sem pontuacao e sem maiusculas

#Casos de teste

#inverte('Comi banana, mamao e morango. Estavam deliciosas') ==
# 'deliciosas estavam morango e mamao banana comi'
#inverte('calculo e uma materia que demanda muito tempo e atencao') ==
# ' atencao e tempo muito demanda que materia uma e calculo