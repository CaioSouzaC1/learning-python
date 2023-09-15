import random


def play():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")

    print("*********************************")
    print("Qual nível de dificuldade você deseja?")

    level = int(input("(1) Fácil | (2) Médio | (3) Difícil "))

    secret_number = int(random.random() * 100)
    times = range(0, 3)
    if (level == 1):
        times = range(0, 10)
    elif (level == 2):
        times = range(0, 6)

    correct = 0
    point = 100
    for time in times:
        print("\n\----- RODADA  {} -----/". format(time + 1))
        chute = input("Digite um número: ")

        if(int(chute) == secret_number):
            print("\n*********************************")
            print("ACERTOU")
            print("*********************************")

            correct = 1
            break
        else:
            point = 100 - ((100/len(times)) * time + 1)
            if int(chute) > secret_number:
                print("ERROU, chute alto")
            else:
                print("ERROU, chute baixo")
        print("\--------------------/")

    if correct == 0:
        print("O Número secreto era ", secret_number)

    print("Sua nota foi de ", point)
    print("\n\nFim do Jogo")
    print("*********************************")
