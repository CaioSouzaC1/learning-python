import adivinhacao
import forca
print("***************************")
print("Escolha um Jogo")
print("***************************")


game = int(input("(1) Adivinhação | (2) Forca "))

if (game == 1):
    adivinhacao.play()
else:
    forca.play()