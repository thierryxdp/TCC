def retira_pontuacao(frase):
    '''Função que recebe uma frase e retorna outra frase com os ccaractere de pontução substituídos por espaço'''
	'''str --> str'''
    x=str.replace(frase,"!"," ")
    y=str.replace(x,","," ")
    z=str.replace(y,"."," ")
    w=str.replace(z,"-"," ")
    w1=str.replace(w,":"," ")
    w2=str.replace(w1,";"," ")
    w3=str.replace(w2,";"," ")
    w4=str.replace(w3,"?"," ")
    return w4