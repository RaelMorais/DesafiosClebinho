import numpy as np
from arts import art
import threading
import time 

class jogo_velhadificl:
    def __init__(self):
        self.a = ""
        self.timer = None
        self.tempo_limite = 5
        self.stop_input_event = threading.Event()
        self.tabuleiro = np.array([["", "", ""], ["", "", ""], ["", "", ""]])
        self.vencer = False 
        self.jogador1 = "X"  
        self.jogador2 = "O"
     
        def opcao():
            escolha = input("1-Play\n2-Quit\n")  
            match escolha:  
                case "1": 
                    jogar() 
                case "2": 
                    art.arts_for_game().asc_art()
                    exit() 
        def stop_input_after_timeout(timeout):
            time.sleep(timeout)  # Wait for the timeout duration
            self.stop_input_event.set()  # Trigger the event to stop the input thread
            print("Time's up! Stopping input.")
        def iniciar_jogada(self, jogador):
            print(f"Vez do jogador {jogador}")
            input_thread = threading.Thread(target=inserirLinhaColuna,args=(jogador,))
            input_thread.start()
            
            # self.timer = threading.Timer(self.tempo_limite, tempo_acabou, [jogador])
            # self.timer.start()
            timeout_thread = threading.Thread(target=stop_input_after_timeout, args=(self.tempo_limite,))
            timeout_thread.start()
            # self.inserirLinhaColuna(jogador)
            # Wait for the timeout thread to finish
            timeout_thread.join()

            # Wait for the input thread to finish
            input_thread.join()

        # Se o jogador fizer a jogada a tempo, cancela o timer
        # O cancelamento é feito após o jogador já ter feito a jogada
            self.timer.cancel()
            
            
        def jogar():#controle de quem joga
            while True:
                mostrarTabuleiro() 
                iniciar_jogada(self.jogador1)
                if checarSeGanhou(self.jogador1):  
                    break  

                mostrarTabuleiro()  
                iniciar_jogada(self.jogador2) 
                if checarSeGanhou(self.jogador2): 
                    break  
        def mostrarTabuleiro():
            art.arts_for_game().jogo_bem_vindo() 
            for i in range(3):  
                linha_display = []  
                for j in range(3):  
                    if self.tabuleiro[i, j] == "":  
                        linha_display.append(f"{i+1},{j+1}")  
                    else:
                        linha_display.append(self.tabuleiro[i, j])  
                print(' ', ' | '.join(linha_display))  
                if i < 2:  
                    print(" --------- ")
        def inserirLinhaColuna(self, jogador):
            while True and not self.stop_input_event.is_set():  
                try:
                    linha = int(input(f'Player {jogador} | Row: '))
                    coluna = int(input(f'Player {jogador} | Column: '))
                    
                    if 1 <= linha <= 3 and 1 <= coluna <= 3:
                        if self.tabuleiro[linha-1, coluna-1] == "":
                            self.tabuleiro[linha-1, coluna-1] = jogador  
                            break  
                        else:
                            print("Position is occupied") 
                    else:
                        print("Row and column must be between 1 and 3") 
                except ValueError:
                    print("Enter a number between 1 and 3.") 

        def checarSeGanhou(jogador):
            if ganharEmLinha(jogador) or ganharEmColuna(jogador) or ganharEmDiagonal(jogador):
                mostrarTabuleiro()  
                print(f'Player {jogador} Wins!') 
                art.arts_for_game().game_art()
                return True 
            if darVelha():  
                mostrarTabuleiro() 
                art.arts_for_game().deuvelha()
                return True 
            return False 
        def ganharEmLinha(jogador):
            for a in range(3):
                if np.all(self.tabuleiro[a, :] == jogador):  
                    return True 
            return False  
        def ganharEmColuna(jogador):
            for k in range(3):  
                if np.all(self.tabuleiro[:, k] == jogador): 
                    return True 
            return False  
        def ganharEmDiagonal(jogador):
            if np.all(np.diag(self.tabuleiro) == jogador): 
                return True
            if np.all(np.diag(np.fliplr(self.tabuleiro)) == jogador):  
                return True
            return False
        def darVelha():
            if np.all(self.tabuleiro != ""): 
                return True 
            return False 
        while True:
            mostrarTabuleiro() 
            iniciar_jogada(self.jogador1)  
            if checarSeGanhou(self.jogador1):  
                break  

            mostrarTabuleiro()  
            iniciar_jogada(self.jogador2)  
            if checarSeGanhou(self.jogador2): 
                break  

        opcao()
