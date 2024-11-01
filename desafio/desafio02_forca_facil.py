# Cores ANSI
RED = "\033[33m"
RESET = "\033[0m"
class ForcaFacil:
    def facil(self):    
        palavra = "Palmeiras"
        dica = "Mundial"
        palavra_escondida = ['*'] * len(palavra)
        print(dica)
        print(f"Quantidade de palavras escondidas: {' '.join(palavra_escondida)}")
        
        tentativas = 6
        palavras_chutadas = []
        
        while tentativas > 0:
            chute = input("Chute uma letra: ").strip().lower()
            try:
                if chute in palavras_chutadas:
                    print("Tente outra letra, essa já foi")
                    continue
                
                palavras_chutadas.append(chute)  # Adiciona a letra chutada à lista

                if chute in palavra.lower():  # Verifica se o chute está na palavra (ignorando maiúsculas)
                    for posicao in range(len(palavra)):
                        if palavra[posicao].lower() == chute:  # Compara a letra chutada com a palavra
                            palavra_escondida[posicao] = palavra[posicao]  # Revela a letra na palavra escondida
                            print("Acertou uma letra!")
                else:
                    tentativas -= 1
                    print(f"Letra errada, você tem {tentativas} chances")
                
                print(f"Palavra: {' '.join(palavra_escondida)}")
                print(f"Letras já chutadas: {', '.join(palavras_chutadas)}")
                # Mostra as letras já chutadas
                if tentativas == 0:
                    print(f"A palavra era {palavra}")
                if '*' not in palavra_escondida:
                    print(f"Você ganhou, a palavra era {RED}{palavra}{RESET}")
                    break
            
            except ValueError:
                print("É culpa do bagre albeeeeeeerto")

