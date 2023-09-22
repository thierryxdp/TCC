def uppCons(frase):
    answer = ""
    letter=0
    for letter in frase:
        if letter not in "aeiouáéíóúãâôõ":
            answer = answer + letter.upper()
        else:
            answer = answer + letter
            letter=letter=1
    return answer


print(uppCons(input("Enter a frase: ")))