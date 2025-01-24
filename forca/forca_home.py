import desafio_forca
def home_desafio02():
        escolha = input("Escolha \n[1] Fácil  \n[2] Médio \n[3] Díficil \n>>>")
        try:
            match escolha:
                    case '1':
                        desafio_forca.Forca().facil()
                    case '2':
                        desafio_forca.Forca().medio()
                    case '3':
                        desafio_forca.Forca().dificil()
                    case _:
                        print("Erro")
        except ValueError as error_value:
                print(error_value)
home_desafio02()