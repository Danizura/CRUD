import customtkinter
import os
from recursos.banco_de_dados.criptografia.cripto import descriptografar_dados,criptografar_dados
from recursos.login.login import  Tela_login
from recursos.banco_de_dados.banco import Funcionario,Clientes

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.funcoes_da_janela()
        self.funcao_inicial()
    def funcao_inicial(self):
        print
        #self.verificar
    def verificar(self):
        usuario_atual=tela_login.usuario_atual
        senha_atual=tela_login.senha_atual
        funcionario=Funcionario()
        usuario_banco=funcionario.listar_funcionarios()[0]
        senha_banco=funcionario.listar_funcionarios()[1]
        if senha_atual==senha_banco and usuario_atual==usuario_banco:
            pass
        else:
            self.destroy()
    def funcoes_da_janela(self):
        self.geometry(f"{self._max_height}x{self._max_width}")
        self.minsize(height=self.winfo_screenheight(),width=self.winfo_screenwidth())
        self.frame()
    def lateral(self):
        #criaçao do frame
        imagem_lateral=customtkinter.CTkFrame(self,fg_color="#242424",width=200,height=800,corner_radius=0)
        imagem_lateral.grid()
    
    def caminho_arquivo(self,path,file):
        diretorio=os.path.dirname(__file__)
        caminho=os.path.join(diretorio,path)
        arquivo=os.path.join(caminho,file)
        return arquivo
#aqui inicia a tela de login

tela_login=Tela_login()
tela_login.mainloop()

#se a tela de login foi destruida inicia a tela do crud


if tela_login.destruiu==True:
    #segunda verificaçao do usuario
    try:
        #pega a senha e o usuario atual e verifica se sao os mesmos 
        usuario_atual=tela_login.usuario_atual
        senha_atual=tela_login.senha_atual
        #aqui tenta descriptografar o usuario do funcionario pra verificar se a senha esta correta
        funcionario=Funcionario()
        usuario_banco=descriptografar_dados(funcionario.listar_funcionarios()[0],usuario_atual)
        senha_banco=descriptografar_dados(funcionario.listar_funcionarios()[1],senha_atual)
        #aqui ira iniciar somente caso a senha do banco de dados e a senha atual conbinar
        if senha_atual==senha_banco and usuario_atual==usuario_banco:
            app=App()
            app.mainloop()
        else:
            pass
    except:
        print("erro no login")    
else:
    pass

