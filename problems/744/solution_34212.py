def hashtag(s):
    '''Recebe uma string e retorna ela mesma com "#" no início, meio e final. str -> str.'''
    return "#"+s[0:len(s)/2]+"#"+s[len(s)/2:]+"#"