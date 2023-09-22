def stringinvert(palavra):
    if len(palavra) < 10:
        print(palavra)
        return stringinvert(palavra[::-1])

print(stringinvert('teste'))