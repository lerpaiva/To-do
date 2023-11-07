from dao import*
class ToDo():


    def AdicionarTarefa(self, tarefa, x, status):
        add = DaoAdicionarTarefa()
        return add.adicionarTarefa(tarefa, x, status)

    def ExcluirTarefa(self, excluir):
        #exclude = DaoExcluirTarefa()
        #return exclude.excluirTarefa(excluir)
        pass
    def ListarTarefa(self):
        return DaoListarTarefa.listarTarefa()
    
    def AlterarTarefa(self, tarefa):
        alt = DaoAlterarTarefas()
        return alt.alterarTarefa(tarefa)


ToDO = ToDo()
