from dao import *
class ToDo():


    def AdicionarTarefa(self, tarefa, x, status):
        add = DaoAdicionarTarefa()
        return add.adicionarTarefa(tarefa, x, status)

    def ListarTarefa(self):
        return DaoListarTarefa.listarTarefa()
    
    def AlterarTarefa(self, tarefa_A, tarefa_alterada):
        alt = DaoAlterarTarefas()
        return alt.alterarTarefa(tarefa_A, tarefa_alterada)
    def ConcluirExcluirTarefa(self,ind,newstats):
        statss = DaoConExcTarefas()
        return statss.conExcTarefa(ind,newstats)


ToDO = ToDo()
