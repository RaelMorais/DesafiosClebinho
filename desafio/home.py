import desafio02_forca_dificil
import desafio02_forca_medio
import desafio02_forca_facil
import prints
class desafio02_home:
    def __init__(self):
         self.a = ""
    def home_desafio02(self):
        prints.printes().printJogo()
        escolha = input("Escolha \n[1] Fácil  \n[2] Médio \n[3] Díficil \n>>>")
        try:
            match escolha:
                    case '1':
                        desafio02_forca_facil.ForcaFacil().facil()
                    case '2':
                        desafio02_forca_medio.medio_forca_classe().medio()
                    case '3':
                        desafio02_forca_dificil.forcaDificil().dificil()
                    case _:
                        print("Erro")
        except ValueError as error_value:
            print(error_value)
            