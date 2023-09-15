import random


def render_title(text):
    print("***************************")
    print(text)
    print("***************************")
    return

def get_secret_word():
    file = open("palavras.txt","r")
    words_arr = [line.strip() for line in file]
    pos = random.randrange(0,len(words_arr))
    file.close()
    return words_arr[pos]


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print("")
def play():

    render_title("Bem vindo ao jogo Forca")
    secret_word = get_secret_word()

    enforcou = False
    acertou = False

    arr = ["_" for w in secret_word]

    print("A palavra tem {} letras\n".format(len(arr)))

    j = 0
    while(not enforcou and not acertou):
        chute = input("Digite uma letra ").lower().strip()
        i = 0

        if chute in secret_word:
            for w in secret_word:
                if w == chute:
                    arr[i] = w
                i += 1
        else:
            j += 1
            desenha_forca(j)
        enforcou = j >= 7
        word = ''
        for w in arr:
            word = word+w+" "
        print(word)
        if "_" not in word:
            acertou = True

    if acertou:
        imprime_mensagem_vencedor()
    else:
       imprime_mensagem_perdedor(secret_word)

    print("Fim do Jogo!")

if(__name__ == '__main__'):
    play()
