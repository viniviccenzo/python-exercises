# Solicitar ao usuário uma string
string = input("Digite uma string: ")

string = string.replace(" ", "").lower()

if string == string[::-1]:
    print("A string digitada é um palíndromo.")
else:
    print("A string digitada não é um palíndromo.")