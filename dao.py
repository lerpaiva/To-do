
arquivo = "To-Do.txt"
    
class DaoAdicionarTarefa:
    def adicionarTarefa(self, tarefa, x, stat):
        cont=-1
        with open(arquivo,"a") as arq:
            arq.write(f"\t{stat} |\t{x} |\t{tarefa}\n")
            return True
       
class DaoListarTarefa:
    def listarTarefa():
        with open(arquivo, "r") as arq:
            linhas = arq.readlines()
        return linhas
            
class DaoAlterarTarefa:
    def alterarTarefa(self, novaTarefa):
        self.novaTarefa = novaTarefa
        with open(arquivo,"a") as arq:
            arq.write(f"{novaTarefa}")
            return True
                    
class DaoExcluirTarefa:
    def excluirTarefa(self,excluir):
        self.excluir = excluir
        with open(arquivo,"a") as arq:
            arq.write(f"{excluir}")
            return True
        
class DaoConcluirTarefa:
    def excluirTarefa(self,concluir):
        self.concluir = concluir
        with open(arquivo,"a") as arq:
            arq.write(f"{concluir}")
            return True