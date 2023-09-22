def hashtag(s):
    m = (len(s)//2)
    return str ("#") + s[0: m] + str ("#") + s[m:(len(s))] + str ("#")
"""adiciona o caractere # no início, meio e fim de uma palavra."""