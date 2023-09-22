def hashtag(s):
    """funcao hashtag, na saida deve conter o caractere de hashtag no inicio, meio e final"""
    ini=str1[:len(str)//2]
    fn=str1[len(str1)//2:]
    str1="#"+ini+"#"+fn+"#"
    str1="#"+str1[:len(str1)//2]+"#"+str1[len(str1)//2:]+"#"
    return str1