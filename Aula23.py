import random
mega = []


def jogo():
    for i in range(6):
        num = int(input("Digite um número de 1 a 60:\n"))
        while num < 1 or num > 60:
            num = int(input("Digite um número de 1 a 60:\n"))
        mega.append(num)


jogo()

megacerto = []


def randomico():
    for i in range(6):
        numqualquer = random.randint(a=1, b=60)
        megacerto.append(numqualquer)


randomico()
print(mega)
print(megacerto)


def certo():
    acerto = 0
    i = 0
    x = 0
    while x < 6:
        if mega[x] != megacerto[i]:
            i += 1
            if i == 5:
                x += 1
                i = 0
        else:
            x += 1
            i = 0
            acerto += 1
        continue
    print(f"Você acertou {acerto} números!")


certo()
