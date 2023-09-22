def hashtag(s):
    '''Função que retorna uma string com # no início, no meio e no final dela'''
    if len(s)%2==0:
        return "#"+[0:len(s)/2]+"#"+s[(len(s)/2):len(s)]+"#"
    else:
        return "#"+s[0:len(s)//2]+"#"+s[len(s)//2:len(s)]+"#"