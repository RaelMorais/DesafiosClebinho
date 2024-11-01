import sys
sys.path.append("C:\\Users\\dsadm\\Desktop\\Nova pasta (2)\\desafio_clebinho_versao_final\desafio\\")#gambiarra = forçando chamar o módulo
import forca_facil
import desafio1_medio
import desafio1_dificil
class home_desafio01:
    def __init__(self):
        self.a = ""
    def home_desafio_01(self):
        escolha = input("Escolha entre os modos: \n1-Fácil \n2-Médio \n3-Nível clebinho \n") #match para escolher a opção
        match escolha:
            case "1":
                print("Desafio 1 Clebinho")
                forca_facil.facil_forca().jogo_adivinhacao_facil()
            case "2":
                desafio1_medio.desafio_medio().jogo_adivinhacao_medio()   
            case "3":
                desafio1_dificil.desafio_dificil().jogo_adivinhacao_dificil()
            case _:
                print("Inválido")