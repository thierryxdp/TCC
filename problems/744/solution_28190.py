#Função retorna uma string S intercalada por um string #
#O código faz essa # aparecer no antes da palavra começar
#No meio dela e no seu final

def hashtag(s):
    '''Função retorna string S intercalada por até 3 #
    string -> string'''
    tamanho=len(s)//2
    return '#'+str(s[0:tamanho])+'#'+str(s[tamanho:])+'#'