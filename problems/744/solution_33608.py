def hashtag(s):
    '''Funcao que insere o caractere "#" no início, no meio e
no final da string;
    str -> str'''
    if(len(s)%2==0):
        s1=str(s[:len(s)//2])
        s2=str(s[len(s)//2:])
        return "#"+s1+"#"+s2+"#"
    else:
        s1=str(s[:(len(s)-1)//2])
        s2=str(s[(len(s)-1)//2:])
        return "#"+s1+"#"+s2+"#"