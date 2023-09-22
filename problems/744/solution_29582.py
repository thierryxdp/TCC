def hashtag(s):
    '''Função que retorna uma string com # no início, no meio e no final dela'''
    if len(s)%2==0:
        return str('#')+[0:len(s)/2]+str('#')+s[(len(s)/2):len(s)]
    else:
        return str('#')+s[0:len(s)//2]+str('#')+s[len(s)//2:len(s)]