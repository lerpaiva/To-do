from controller import *
import os
sair = 0
while sair == 0:
   
   print("SOFTWARE LISTA TO-DO")
   print("[1] Adicionar tarefas \n[2] Listar tarefas \n[3] Excluir \n[4] Sair")
   print("")
   menu = input("O que deseja fazer>> ")
   match menu:
        case "1":
         os.system("cls")
         print("--ADICIONAR TAREFA--")
         print("")
         tarefa = input("Adicione uma tarefa: ")
         adicionarTarefa = ControllerAdicionarTarefa(tarefa)
         os.system("pause")
        case "2":
         os.system("cls")
         print("--LISTA DE TAREFAS--")
         print("")
         ListarTarefa = ControllerListarTarefa()
         os.system("pause")
        case "3":
         os.system("cls")
         print("--EXCLUIR TAREFA--")
         print("")
         ListarTarefa = ControllerListarTarefa()
         excluir = input("Qual tarefa deseja excluir (índice): ")
         excluirTarefa = ControllerExcluirTarefa(excluir)
         listarTarefa = ControllerListarTarefa()
         os.system("pause")

        case "4":
         sair = 1
        case _:
         os.system("cls")
         print("Opção inválida")
         os.system("pause")


    