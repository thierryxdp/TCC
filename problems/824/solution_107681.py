def uppCons(frase):
    answer = ""
    for letter in frase:
        if letter not in "aeiouAEIOU":
            answer = answer + letter.upper()
        else:
            answer = answer + letter
    return answer


print(toggle(input("Enter a frase: ")))