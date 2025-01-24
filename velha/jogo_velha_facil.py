import numpy as np
from arts import art
class jogo_velhafacil:
    def __init__(self):
        self.a = ""
    def velha_facil(self):
        tabuleiro = np.array([["", "", ""], ["", "", ""], ["", "", ""]])
        vencer = False 
        jogador1 = "X"  
        jogador2 = "O" 
        def opcao():
            escolha = input("1-Play\n2-Quit\n")  
            match escolha:  
                case "1": 
                    jogar() 
                case "2": 
                    art.arts_for_game().asc_art()
                    exit() 

        def jogar():
            while True:
                mostrarTabuleiro() 
                inserirLinhaColuna(jogador1) 
                if checarSeGanhou(jogador1):  
                    break  

                mostrarTabuleiro()  
                inserirLinhaColuna(jogador2)  
                if checarSeGanhou(jogador2): 
                    break  
        def mostrarTabuleiro():
            art.arts_for_game().jogo_bem_vindo() 
            for i in range(3):  
                linha_display = []  
                for j in range(3):  
                    if tabuleiro[i, j] == "":  
                        linha_display.append(f"{i+1},{j+1}")  
                    else:
                        linha_display.append(tabuleiro[i, j])  
                print(' ', ' | '.join(linha_display))  
                if i < 2:  
                    print(" --------- ")
        def inserirLinhaColuna(jogador):
            while True:  
                try:
            
                    linha = int(input(f'Player {jogador} | Row: '))
                    coluna = int(input(f'Player {jogador} | Column: '))
                    
                    if 1 <= linha <= 3 and 1 <= coluna <= 3:
                        if tabuleiro[linha-1, coluna-1] == "":
                            tabuleiro[linha-1, coluna-1] = jogador  
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
                if np.all(tabuleiro[a, :] == jogador):  
                    return True 
            return False  
        def ganharEmColuna(jogador):
            for k in range(3):  
                if np.all(tabuleiro[:, k] == jogador): 
                    return True 
            return False  
        def ganharEmDiagonal(jogador):
            if np.all(np.diag(tabuleiro) == jogador): 
                return True
            if np.all(np.diag(np.fliplr(tabuleiro)) == jogador):  
                return True
            return False
        def darVelha():
            if np.all(tabuleiro != ""): 
                return True 
            return False 
        opcao()