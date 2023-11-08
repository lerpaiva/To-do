from controller import *
arquivo = "To-Do.txt"
    
class DaoAdicionarTarefa:
    def adicionarTarefa(self, tarefa, x, stat):
        with open(arquivo,"a") as arq:
            arq.write(f"{stat} |\t{x} |\t{tarefa}\n")
            return True
       
class DaoListarTarefa:
    def listarTarefa():
        with open(arquivo, "r") as arq:
            linhas = arq.readlines()
        return linhas
            
class DaoAlterarTarefas:
    def alterarTarefa(self, antes, att):
        with open(arquivo, "r") as arq:
            lista = arq.read()

        tudoAtt = lista.replace(antes, att)
        with open(arquivo, "w") as arqui2:
            arqui2.write(tudoAtt)
        return True
    
class DaoConExcTarefas:
    def conExcTarefa(self, antes, att):
        with open(arquivo, "r") as arq:
            lista = arq.read()

        tudoAtt = lista.replace(antes, att)
        with open(arquivo, "w") as arqui2:
            arqui2.write(tudoAtt)
        return True