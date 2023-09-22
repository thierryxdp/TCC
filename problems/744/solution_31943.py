def hashtag(s):
    """funçao que recebe uma string e insera o caractere ”#” no in ́ıcio, no meio
e no final dela"""
    m=(int(len(s)))//2
    return "#"+s[:m]+"#"+s[m:]+"#"