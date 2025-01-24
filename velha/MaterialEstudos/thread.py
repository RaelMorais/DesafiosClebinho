import threading
import time 
def tarefa():#criando tarefa de execução de thread
    for i in range(10):
        print(f"Tarefa em execução: {i}")
        time.sleep(0.5) #tempo de espera entre uma execução e outra 
# user_temp = int(input("Qual o tempo em segundos? "))
def carro1():
    for i in range(10):
        print("Carro 1 está correndo...")
        time.sleep(0.5)
def carro2():
    for i in range(10):
        print("Carro 2 está correndo...")
        time.sleep(0.5)
minha = threading.Thread(target=tarefa)
carro2 = threading.Thread(target=carro2)
carro1 = threading.Thread(target=carro1)
carro1.start()
minha.start()
carro2.start()
carro2.join()
carro1.join()#startando a thread para execução 
minha.join()
# if minha.is_alive():
#     print(f"A tarefa foi executada por {user_temp} segundos")
# else:
#     print("Foi concluida no tempo limite")
    
#percorrer os segundos com um tempo de espera de 0.5ms por execução 