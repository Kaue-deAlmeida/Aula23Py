import random

dados = []
dadosmais = []


def dado():
    numdado = int(input("Escolha um número entre 2 e 12:\n"))
    dados.append(numdado)
    match numdado:
        case 2 | 12:
            porc = (1/36) * 100
            print(f"{porc:.2f}%")
        case 3 | 11:
            porc = (2 / 36) * 100
            print(f"{porc:.2f}%")
        case 4 | 10:
            porc = (3 / 36) * 100
            print(f"{porc:.2f}%")
        case 5 | 9:
            porc = (4 / 36) * 100
            print(f"{porc:.2f}%")
        case 6 | 8:
            porc = (5 / 36) * 100
            print(f"{porc:.2f}%")
        case 7:
            porc = (6 / 36) * 100
            print(f"{porc:.2f}%")
    for i in range(2):
        doisdados = random.randint(a=1, b=6)
        dadosmais.append(doisdados)
    print(sum(dadosmais))


for n in range(1000):
    dado()
