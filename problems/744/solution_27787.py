# Fun ̧c~ao que receba uma string e insira o caractere "#" no in ́ıcio, no meio e no
# final dela.
# str -> str
def hashtag(string):
pos = len(string)//2
return "#" + string[:pos] + "#" + string[pos:] + "#"