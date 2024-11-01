ALGO = "\033[33m"
RESET = "\033[0m"

class medio_forca_classe:
    def medio(self):
        palavra = "Kauan"
        dica = "Maior admirador do comunismo"
        palavra_escondida = ['*'] * len(palavra)
        print(dica)
        print(f"Quantidade de palavras escondidas: {' '.join(palavra_escondida)}")

        tentativas = 6
        palavras_chutadas = []

        while tentativas > 0:
            try:
                chute = input("Chute uma letra: ").strip().lower()
                if chute in palavras_chutadas:
                    print("Tente outra letra, essa já foi.")
                    continue
                palavras_chutadas.append(chute)

                if chute in palavra.lower():
                    for posicao in range(len(palavra)):
                        if palavra[posicao].lower() == chute:
                            palavra_escondida[posicao] = chute
                    print("Acertou!")
                else:
                    tentativas -= 1
                    print("Letra errada!")
                    if tentativas == 5:
                        print("-----")
                        print("|   |")
                        print(" O  |")
                        print("    |")
                        print("    |")
                        print("    |")
                        print("-----")
                    elif tentativas == 4:
                        print("-----")
                        print("|   |")
                        print(" O  |")
                        print(" |  |")
                        print("    |")
                        print("    |")
                        print("-----")
                    elif tentativas == 3:
                        print("-----")
                        print("|   |")
                        print(" O  |")
                        print("/|  |")
                        print("    |")
                        print("    |")
                        print("-----")
                    elif tentativas == 2:
                        print("-----")
                        print("|   |")
                        print(" O  |")
                        print("/|\\ |")
                        print("    |")
                        print("    |")
                        print("-----")
                    elif tentativas == 1:
                        print("-----")
                        print("|   |")
                        print(" O  |")
                        print("/|\\ |")
                        print("/  |")
                        print("    |")
                        print("-----")
                    elif tentativas == 0:
                        print("-----")
                        print("|   |")
                        print(" O  |")
                        print("/|\\ |")
                        print("/ \\ |")
                        print("    |")
                        print("-----")
                        print(f"Você perdeu! A palavra era: {ALGO}{palavra}{RESET}")
                print(f"Palavra: {' '.join(palavra_escondida)}")

                if '*' not in palavra_escondida:
                    print(f"Você ganhou! A palavra era {ALGO}{palavra}{RESET}")
                    break
            except ValueError as erro:
                print(f"Seu erro é {erro}")