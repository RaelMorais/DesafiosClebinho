import random
import printes_home
class Adivinhacao:
    def __init__(self):
        self.a =""
        
    def jogo_adivinhacao_facil(self):
        std = '''
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++
        +                                                     +   
        +                JOGO DA ADIVINHAÇÃO                  +
        +                                                     +
        +    VC POSSUI 5 CHANCES, 100 DE VIDA E UM SONHO!     +
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++
        '''
        print(std)
        #erro na hora de importar random, random tava importando dois valores por estar duplicada, então rodava mas depois ocorria erro
        num = random.randint(1, 101) 
        vida = 100 
        chances = 0
        
        while True:
            try:
                chute = int(input("Acerte o número: "))  
                chances += 1
                
                if chute == num:
                    print("Parabéns, você acertou!")
                    break  # sai do loop se o jogador acertar
                
                
                if chute < num: # atualiza a vida do jogador
                    vida -= (num - chute)
                    print(f"Você errou! O número é maior. \nVida Atual = {vida} \nRodada = {chances}")
                else:
                    vida -= (chute - num)
                    print(f"Você errou! O número é menor. \nVida Atual = {vida} \nRodada = {chances}")
                
                # verifica se o jogador perdeu todas as chances ou vida
                if chances == 5 or vida <= 0:
                    print("Você perdeu! O número era:", num)
                    break
            
            except ValueError:
                print("Erro: Insira um número válido.")  # Mensagem de erro se a entrada não for um número
    def jogo_adivinhacao_medio(self):
        vida = 100
        chances = 0
        num = random.randint(1, 101)
        nomeJogador = input("Qual o seu nome? ")
        
# erro antigo: chance tava duplicada então chamava duas vezes
# entao quando o jogador tentava um número acrescentava mais 2 chances 
# logica do if estava "se o jogador ou o jogador for manor uq eo num soma"
        while True:
            try:
                chute = int(input("Acerte o número: ")) 
                chances += 1
                
                if chute == num:
                    print("Parabéns, você acertou!")
                    break  
                if chute < num:
                    vida -= (num - chute)
                    print(f"Você errou! O número é maior. \nVida Atual = {vida} \nRodada = {chances}")
                else:
                    vida -= (chute - num)
                    print(f"Você errou! O número é menor. \nVida Atual = {vida} \nRodada = {chances}")
                
                if chances == 5 or vida <= 0:
                    print("Você perdeu! O número era:", num)
                    break
            
            except ValueError:
                print("Erro: Insira um número válido.")  

        
        with open('ranking.txt', 'a') as r:
            if vida < 0:
                r.write(f'{nomeJogador} é tão ruim que não consigo marcar a pontuação\n')
            else:
                r.write(f'{nomeJogador} fez {vida} pontos\n')
                
        with open('ranking.txt', 'r') as r:
            ranking = r.readlines()
        
        print("Ranking dos jogadores:")  # RANKING JOGADORES
        for i, linha in enumerate(ranking, start=1):
            print(f"{i}. {linha.strip()}")
    def jogo_adivinhacao_dificil(self):
        # ordenação no rankin estava errada, ela deve salvar antes de jogar no txt
        #vairvael de numero de jogaodres estava somando por algum motivo, então somava o número do jogador ??
        while True:
            try:
                num_jogadores = int(input("Número de jogadores (1-8): "))
                if 1 <= num_jogadores <= 8:
                    break
                elif num_jogadores == 1910:
                    while True:
                        senha = input("Qual o melhor time de SP? ")
                        match senha.lower(): 
                            case 'palmeiras':
                                try: 
                                    printes_home.teste().bbb()
                                    break
                                except ValueError:
                                    printes_home.teste().erro()
                            case 'curintia':
                                try: 
                                    printes_home.teste().aaa()
                                    break
                                except ValueError:
                                    printes_home.teste().erro() 
                            case 'santos':
                                try: 
                                    printes_home.teste().ccc()
                                    break
                                except ValueError:
                                    printes_home.teste().erro() 
                            case _:
                                print("Errado, acesso negado")
                else:
                    print("Número inválido, deve ser entre 1 e 8.")
            except ValueError:
                print("Erro: Insira um número válido.")
        jogadores = []
        for i in range(num_jogadores):
            nomeJogador = input(f"Qual o seu nome do jogador {i + 1}? ")
            jogadores.append((nomeJogador, 100))  

        num = random.randint(1, 101)  
        chance = 0
        while True:
            for i, (nomeJogador, vida) in enumerate(jogadores):
                if vida <= 0:
                    print(f"{nomeJogador} está sem vida.")
                    continue

                print(f"\nVez de {nomeJogador}:")

                try:
                    chute = int(input("Acerte o número: "))
                    chance += 1

                    if chute == num:
                        print("Parabéns, você acertou!")
                        break
                    else:
                        perda = abs(num - chute)
                        vida -= perda
                        jogadores[i] = (nomeJogador, max(0, vida))  # Atualiza a vida do jogador
                        print(f"Você errou! Vida Atual = {vida} \nPossui = {chance} chances")

                    if chance >= 5:
                        print("Você não tem mais chances.")
                        break

                except ValueError:
                    print("Insira um número válido.")

            if chance >= 5 or all(vida <= 0 for _, vida in jogadores):
                break

        with open('ranking.txt', 'w') as r:
            for nomeJogador, vida in sorted(jogadores, key=lambda x: x[1], reverse=True):
                if vida <= 0:
                    r.write(f'{nomeJogador} é tão ruim que não consigo marcar a pontuação\n')
                else: 
                    r.write(f"{nomeJogador} fez {vida} pontos\n")

            try:
                with open('ranking.txt', 'r') as r:
                    ranking = r.readlines()
                    ranking.sort(reverse=True)
                    for i, linha in enumerate(ranking, start=1):
                        if i == 1:
                            r.write(f"**Campeão**: {nomeJogador} fez {vida} pontos\n")
                        elif i == len(jogadores):
                            r.write(f"**Último lugar**: {nomeJogador} fez {vida} pontos\n")
                        print(f"{i}. {linha.strip()}")
            except FileNotFoundError:
                print("Erro.")
