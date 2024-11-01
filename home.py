import sys
sys.path.append("C:\\Users\\dsadm\\Desktop\\Nova pasta (2)\\desafio_clebinho_versao_final\\desafio")
sys.path.append("C:\\Users\\dsadm\\Desktop\\Nova pasta (2)\\desafio_clebinho_versao_final\\sgpt")
from desafio import relogio
from sgpt import gemini
from desafio import desafio_clebinho
from desafio import home

import hello

asc_art = '''
    >>>>>>>VERSÃO 2.0<<<<<<<<<<
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⣋⣉⡙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠮⡞⠁⠀⠈⢢⠷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢠⢤⣇⠀⡇⠀⠀⠀⢸⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⡏⢰⠙⠚⢧⣀⢀⣠⠞⠓⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⡸⠀⡎⠀⣀⡤⠏⠉⠧⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢠⠃⢰⡵⠊⠁⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢸⡀⠀⣀⡠⡆⠀⠀⠀⠀⠀⣆⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⡇⠀⠀⠀⠀⠀⡏⢣⡀⠘⣄⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⢸⠀⠙⢤⡈⢦⡀⠀⠀⠀⠀⠀⠀ 
⠀⠀⢠⠖⣒⣶⠖⠒⠒⠒⠲⠷⣒⠒⠒⠒⠒⣺⣶⠖⠒⠓⢤⣹⠶⣒⠲⡄⠀⠀ 
⠀⢠⠏⣞⣟⠉⠀⣖⠒⣲⠀⠀⠈⣳⠀⠀⡎⡞⠉⠀⣖⢒⣢⠀⠀⠈⡇⠹⡄⠀ 
⢠⠏⠀⠘⠪⢅⣀⣀⠉⣀⣀⡠⠔⠁⠀⠀⠙⠮⣇⣀⣀⠉⣀⣀⡤⠖⠁⠀⠹⡄ 
⡟⠒⠒⠒⠒⠒⠒⠓⠛⠚⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠚⠛⠛⠒⠒⠒⠒⠒⠒⢻ 
⣇⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣸
    >>>>>FUNCIONOU<<<<<<<<<<<
''' 
print(asc_art)
escolha = input("Escolha\n1-Desafio 1\n2-Desafio 2\n3-Desafio 3\n4-Hello\n5-Relogio\n")
match escolha:
    case "1":
        desafio_clebinho.home_desafio01().home_desafio_01()
    case "2":
        home.desafio02_home().home_desafio02()
    case "3":
        print("Até logo!")
        exit()
    case "4":
        hello.home_hell0().hello_home()
    case "5":
        relogio.relogio_funcao().relogioooooo()
    case "6":
        
        
        