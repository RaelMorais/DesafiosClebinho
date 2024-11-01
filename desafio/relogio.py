from tkinter import *
from tkinter import ttk
import datetime as dt
class relogio_funcao:
        def __init__(self):
             self.a = ""
        def relogioooooo(self):
            dia_semana = dt.date.today().weekday()

            dias_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")

            if dia_semana in {5,6}:
                variavel_semana = dias_semana[dia_semana]
                variavel_semana = "É FDS PÇR VAI DORMIR" + variavel_semana
            elif dia_semana in {4}:
                variavel_semana = dias_semana[dia_semana]
                variavel_semana = "SEXTOOOOOU HOJE É " + variavel_semana
            else:
                variavel_semana = dias_semana[dia_semana]
                variavel_semana = "Hoje é" + variavel_semana

            def time_now():
                hora_atual = dt.datetime.now().strftime('%H:%M:%S')
                time_label.config(text=hora_atual)  # Atualiza o texto do rótulo
                time_label.after(1000, time_now) 
            def date_now():
                data_atual = dt.datetime.now().strftime('%d/%m/%Y')
                data_label.config(text=data_atual)

            root = Tk()
            frm = ttk.Frame(root, padding=200)
            frm.grid()
            time_label = ttk.Label(frm, font='Helvetica 20 bold')
            time_label.grid(column=0, row=1)  
            data_label = ttk.Label(frm, font='Helvetica 20 bold')
            data_label.grid(column=0, row=2)


            ttk.Label(frm, text=variavel_semana, font='Helvetica 20 bold').grid(column=0, row=0)
            ttk.Button(frm, text="Sair", command=root.destroy).grid(column=0, row=3)
            time_now()
            date_now()
            root.mainloop()