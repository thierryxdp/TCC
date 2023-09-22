def hashtag(s):
    str = input ("quimica:")
    str = "#" + str + "#"
    meio = lent(str) // 2
    str = [:meio] + "#" + str[meio:]