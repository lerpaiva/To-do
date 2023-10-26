from controller import *
import os
sair = 0
while sair == 0:
   
   print("SOFTWARE LISTA TO-DO")
   print("[1] Adicionar tarefas \n[2] Listar tarefas \n[3] Alterar tarefa \n[4] Concluir Tarefa \n[5] Listar tarefas concluídas \n[6] Excluir tarefas \n[7] Sair")
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
          print("--ALTERAR TAREFAS--")
          print("")
          ListarTarefa = ControllerListarTarefa()
          qual = input("Digite o índice da tarefa que deseja alterar: ")
          novaTarefa = input("Nova tarefa: ")
          alterarTarefa = ControllerAlterarTarefa(qual, novaTarefa)
          os.system("pause")
        case "4":
          os.system("cls")
          print("--CONCLUIR TAREFAS--")
          print("")
          ListarTarefa = ControllerListarTarefa()
          print("Digite o índice da tarefa que deseja marcar como concluída")
          qual = input(">> ")
          ConcluirTarefa = ControllerConcluirTarefa(qual)
          os.system("pause")
        case "5":
          os.system("cls")
          print("--TAREFAS CONCLUÍDAS--")
          print("")
          ListarTarefa = ControllerTarefasConcluidas()
          os.system("pause")
        case "6":
         os.system("cls")
         print("--EXCLUIR TAREFA--")
         print("")
         ListarTarefa = ControllerListarTarefa()
         print("Digite o índice da tarefa que deseja excluir")
         qual = input(">> ")
         ConcluirTarefa = ControllerExcluirTarefa(qual)
         os.system("pause")

        case "7":
         sair = 1
        case _:
         os.system("cls")
         print("Opção inválida")
         os.system("pause")


    