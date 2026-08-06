                                                                                                                                                                                                                                                                                                                                                  
print("\t=================================")
print("\tBem Vindo Ao Atlas Academy")         #Mensagem Para saber qual modulo estamos
print("\t================================")

                                                        #inplementar a função para listar todo o conteudo
                                                        #implementar a função para sair do programa
                                                        #corrigir falha de entrada da função do menu
                                                        #colocar os dicionario em uma clase só
 #Função De Menu Do usúario           
def menu(): 
    print("\n======================================\n")
    print("1- Registrar Estudo \n") #criando o menu
    print("=======================================\n")
    print("2- Adcionar Notas \n")
    print("========================================\n")
    print("3- Listar Estudo\n")
    print("=========================================\n")
    print("4- Sair\n")
    entrada = int(input("Escolha Uma Opção:")) #salvando a opção do usuario na variavel entrada
    return entrada #retornando a escolha do usuario para usar em outra função

#criando uma classe para  objeto Atlas  para criar uma lista 
class registro_estudo:
       def __init__ (self):
           self.dic = []
           self.dic2 = []

#cada função de op1 até op3  realiza uma ação após a opção do usuario op1(self): 
       def op1(self):
              print("Você Escolheu Registrar Estudo\n")
              Registro = input("O Que Você Estudou Hoje?: ").strip()
              Hora  = input("\nQuantas Horas Você Estudou Hoje?: ").strip()
              Dia  =  input("\nQue Dia  É Hoje?: ").strip()
              #verificando se todos os dados foram prenchidos
              if Registro != "" and Hora != ""  and Dia != "":
                           self.dic.append({"Materia":Registro, "Horario": Hora, "Data": Dia})  #atribuindo as informações para o dicionario
                           print("Parabéns Você Realizou O Registro DO  Seu Estudo de Hoje\n")
                           return self.dic
              else:
                print("Você Não Concluiu Ou Não Escreveu Os Dados\n")
                return True


       #Função Para O Usuario Adcionar Uma Nota e Guardar Dentro de um dicionario
       def op2(self):
                print("Você Escolheu Escrever Uma Anotação\n")
                nota = input("Escreva A Sua Anotação: ").strip()
                if nota != "":
                        self.dic2.append({"Notas": nota})
                        return self.dic2
                        print("A Sua Anotação Foi Salva")
                else:
                  print("Você Não Anotou Nada Na Nota") #vericando se o usuario Digitou algo na nota, se estiver vazio mostra o aviso 
                  return True

       def op3(self):
                #percorrendo a lista
                for i in self.dic:

                        #percorrendo os valores da lista usando a função itemss para organizar os dados
                        for chave,valor in i.items():
                               print(f"{chave}: {valor}")

                        for di2 in self.dic2:
                                for nots,nota in di2.items():
                                        print(f"{nots}: {nota}")
      
#Função Para O Usuario Sair Do Programa 
       


#Função para verificar a escolha do usúario Para Registrar O Estudo

def check(escolha,self):
    if escolha == 1: #verificando a escolha do usuario
              self.op1()
              return True

    elif  escolha == 2: #Verificando A Segunda Escolha do usúario
              self.op2()
              return True

    elif  escolha == 3:
              self.op3()
              return True
    if escolha == 4:
           print("VocÊ Saiu")
           return False
    else:
        print("Opção Inválida")
        return False
#Atribuindo O Objeto 
atlas = registro_estudo()


while True:
        escolha = menu()   #pegando o valor retornado da função menu para usar em outra função

        opcao =  check(escolha,atlas)#pegando o valor retornado da opção do usúario e atribuindo a variavel opção, e passando o dicionario
        if opcao  == False: #verficando a opção retornada para ver se é falsa
                break





































