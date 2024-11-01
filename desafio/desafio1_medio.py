import random
class desafio_medio:
    def __init__(self):
        self.a = ""
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
    