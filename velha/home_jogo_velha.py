from arts import art
import jogo_velha_facil
import jogo_velha_dificil

def menu():
    option = input("Choose an option: \n1-Play \n2-Play with time \n3-Exit\n")
    match option:
        case"1":
            jogo_velha_facil.jogo_velhafacil().velha_facil()
        case"2":
            jogo_velha_dificil.jogo_velhadificil().opcao()
        case"3":
            art.arts_for_game().asc_art()
            exit()
menu()
