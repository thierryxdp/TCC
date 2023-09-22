def hashtag(s):
    """funcao hashtag, na saida deve conter o caractere de hashtag no inicio, meio e final"""
    ini=s[:len(s)//2]
    fn=s[len(s)//2:]
    s="#"+s[:len(s)//2]+"#"+s[len(s)//2:]+"#"
    return s