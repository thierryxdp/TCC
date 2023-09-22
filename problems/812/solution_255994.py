def retira_travessao(frase):
    '''Função que retira o travessão de uma string e substitui ela por espaço'''
    return str.replace(frase,"_"," ")

def retira_virgula(frase):
    '''Função que retira a vírgula de uma string e substitui ela por espaço'''
    return str.replace(frase,","," ")

def retira_dois_pontos(frase):
    '''Função que retira os dois pontos de uma string e substitui ela por espaço'''
    return str.replace(frase,":"," ")

def retira_ponto_virgula(frase):
    '''Função que retira o ponto e virgula de uma string e substitui ela por espaço'''
    return str.replace(frase,";"," ")

def retira_ponto_final(frase):
    '''Função que retira o ponto final de uma string e substitui ela por espaço'''
    return str.replace(frase,"."," ")

def retira_exclamacao(frase):
    '''Função que retira o ponto de exclamação de uma string e substitui ela por espaço'''
    return str.replace(frase,"!"," ")

def retira_interrogacao(frase):
    '''Função que retira o ponto de interrogação de uma string e substitui ela por espaço'''
    return str.replace(frase,"?"," ")

def retira_pontos(frases):
    '''Função que retira pontos de uma frase'''
    return retira_travessao + retira_virgula + retira_dois_pontos + retira_ponto_virgula + retira_ponto_final + retira_exclamacao + retira_interrogacao

def retira_pontuacao(frases):
    '''Função que dada uma frase susbstitui todos os pontos por espaço'''
    return retira_pontos