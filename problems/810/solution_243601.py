def retira_pontuacao(frase):
    f1 = str.replace(frase,"?"," ")
    f2 = str.replace(f1,"."," ")
    f3 = str.replace(f2,"!"," ")
    f4 = str.replace(f3,":"," ")
    f5 = str.replace(f4,";"," ")
    f6 = str.replace(f5,"-"," ")
    f7 = str.replace(f6,","," ")
    return f7
def inverte(frase):
    ''' Função que recebe uma string "frase", e retorna uma string
    contendo os elementos da string original, porém com as palavras
    na ordem inversa'''
        #casos de teste:
    ''' inverte("Jájá eu termino o MT")
    ->  'MT o termino eu Jájá'
        inverte("Socorram-me subi no onibus em Marrocos")
        'Marrocos em onibus no subi Socorram-me'
        inverte("Achei que daria certo o ex anterior")
        'anterior ex o certo daria que Achei' '''
    NF=retira_pontuacao(frase)
    Fm=str.lower(NF)
    Fs=str.split(Fm)
    list.reverse(Fs)
    Li=Fs
    Fi=str.join(" ", Li)
    return Fi