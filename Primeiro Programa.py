x = 4
idade = 4
objeto = "palhaço"

lista = [objeto, idade, x]
lista[2]

lista_mista = ["cavalo", "pato", 16, 17]
animal = []
numero = []

for item in lista_mista:
    if type(item) == str:
        animal.append(item)
    elif type(item) == int:
        numero.append(item)

animal[0]
lista_mista = [20,30,50,10,"cavalo", "pato", 16, 17]
i = 0

while i < len(lista_mista):
    if isinstance(lista_mista[1], str):
        print()
