def uppCons(phrase):
    answer = ""
    for letter in phrase:
        if letter not in "aãeéêiíoóôõuAEIOU":
            answer = answer + letter.upper()
        else:
            answer = answer + letter
    return answer