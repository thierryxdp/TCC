# Retorna a string com # (hashtag) no  início, meio e final dela.
# É colocado a hashtag no começo, concatenado a string até o meio dela, concatenado outra hashtag,
# concatenado a string até o final dela, e então concatenado outra hashtag
# str-> str
def hashtag(s):
    metadeString = len(s) // 2
    return '#' + s[:metadeString] + '#' + s[metadeString:] + '#'