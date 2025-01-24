import desafio_adivinhacao
def home_desafio01():
        escolha = input("Escolha \n[1] Fácil  \n[2] Médio \n[3] Díficil \n>>>")
        try:
            match escolha:
                    case '1':
                        desafio_adivinhacao.Adivinhacao().jogo_adivinhacao_facil()
                    case '2':
                        desafio_adivinhacao.Adivinhacao().jogo_adivinhacao_medio()
                    case '3':
                        desafio_adivinhacao.Adivinhacao().jogo_adivinhacao_dificil()
                    case _:
                        print("Erro")
        except ValueError as error_value:
                print(error_value)
home_desafio01()