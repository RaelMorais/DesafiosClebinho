import random
class facil_forca:
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
            return facil_forca