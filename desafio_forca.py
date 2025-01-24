RED = "\033[33m"
RESET = "\033[0m"
import random
class Forca:
    def __init__(self):
        self.a = "" 
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
                        print(f"Você perdeu! A palavra era: {RED}{palavra}{RESET}")
                print(f"Palavra: {' '.join(palavra_escondida)}")

                if '*' not in palavra_escondida:
                    print(f"Você ganhou! A palavra era {RED}{palavra}{RESET}")
                    break
            except ValueError as erro:
                print(f"Seu erro é {erro}")
    def dificil(self):
        palavras_dicas = {}
        
        # Carregar palavras e dicas do arquivo
        with open('palavras.txt', 'r', encoding='utf-8') as file:
            for linha in file:
                linha = linha.strip().lower()
                try:
                    palavra, dica = linha.split(';') 
                    palavras_dicas[palavra] = dica
                except ValueError as erro_value:
                    print(erro_value)
        
        # Menu de opções para o usuário
        escolha = input(">>>Escolha abaixo<<<\n1 - Jogar\n2 - Adicionar palavra\n3 - Remover Palavra\n4 - Sair\n")
        
        match escolha:
            case '1':
                # Jogar
                palavra = random.choice(list(palavras_dicas.keys()))
                dica = palavras_dicas[palavra]
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

                        if chute in palavra: 
                            for posicao in range(len(palavra)):
                                if palavra[posicao] == chute:  
                                    palavra_escondida[posicao] = chute  
                        else:
                            tentativas -= 1
                            print(f"Letra errada, você tem {tentativas} chances")
                        
                        print(f"Palavra: {' '.join(palavra_escondida)}")
                        
                        if '*' not in palavra_escondida:
                            print(f"Você ganhou, a palavra era {RED}{palavra}{RESET}")
                            break
                    except ValueError as value_erro:
                        print(value_erro)
                else:
                    print(f"Você perdeu, a palavra era {palavra}")

            case '2':    
                # Adicionar nova palavra e dica
                num_palavras = int(input("Qual o número de palavras a serem adicionadas? "))
                for _ in range(num_palavras):
                    nova_palavra = input("Qual a nova palavra? ").strip().lower()
                    nova_dica = input("Qual a dica dessa palavra? ").strip().lower()
                    palavras_dicas[nova_palavra] = nova_dica
                
                # Salvar novas palavras e dicas no arquivo
                with open('palavras.txt', 'a', encoding='utf-8') as file:
                    for nova_palavra, nova_dica in palavras_dicas.items():
                        file.write(f'{nova_palavra};{nova_dica}\n')

            case '3':
                # Remover palavra
                while True:
                    print(">>>Entre com senha ou usuario<<<")
                    user = input("Digite seu usuario: ")
                    password = input("Digite sua senha: ")
                    if user == "admin" and password == "123456":
                        print(f"Bem vindo {user}, aqui pode remover palavra")
                        remover_palavra = input("Qual palavra vai ser removida? ").strip().lower()
                        if remover_palavra in palavras_dicas:
                            del palavras_dicas[remover_palavra]
                            # Salvar as palavras restantes no arquivo
                            with open('palavras.txt', 'w', encoding='utf-8') as file:
                                for p, d in palavras_dicas.items():
                                    file.write(f'{p};{d}\n')
                            print(f"Palavra {remover_palavra} foi removida.")
                        else:
                            print("Palavra não reconhecida.")
                        break
                    else:
                        print("Acesso negado")

            case '4':
                print("Você está saindo...")
                exit()

            case _:
                print("Erro: Opção inválida.")