def aspasConveter(string):
    res = ""
    for i in range(0, len(string)):
        if string[i] == "'":
            res += '"'
        else:
            res += string[i]
    print(res)


aspasConveter("{'1': {'Idade': 21, 'Nome': 'Felipe', 'Sexo:': 'M'}, '2': {'Idade': 52, 'Nome:': 'Lu', 'Sexo': 'F'}, '-NFU0RsWTzy6PhLBofru': {'Idade': '39', 'Nome': 'Joca', 'Sexo': 'M'}}")
