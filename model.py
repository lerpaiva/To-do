from dao import*
class ToDo():


    def AdicionarTarefa(self, tarefa, x, status):
        add = DaoAdicionarTarefa()
        return add.adicionarTarefa(tarefa, x, status)

    #def ExcluirTarefa(self, excluir):
     #   self.lista.pop(excluir)
     #   return True

    def ListarTarefa(self):
        return DaoListarTarefa.listarTarefa()
    
    def AlterarTarefa(self, tarefa):
        alt = DaoAlterarTarefa()
        return alt.alterarTarefa(tarefa)


ToDO = ToDo()
