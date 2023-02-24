class Driver:
    def __init__(self,nome):
        self.nome=nome
    
    def Dirigir(self,carteira,idade):
        if carteira == True and idade >18:
            print('\033[30;42m Está pronto para dirigir, Parabéns\033[m')
        elif carteira == True and idade < 18:
            print('\033[45m OLOKO!! \033[m Quem te deixou dirigir {}?\n \033[31;40mNão pode\033[m'.format(self.nome.title()))
        else:
            print('\033[31;40mNão pode dirigir\033[m')
nome=""
idade=0
motorista = Driver(nome)
motorista.nome=str(input('Digite seu nome: '))

idade=int(input('Digite sua idade {}: '.format(motorista.nome.title())))

teste=str(input('Digite Y se você tem carteira de motorista ou N se não tiver: '))

if teste == "Y" or teste == "y" and idade >18:
    motorista.Dirigir(True,idade)
elif teste == "N" or teste == "n" and idade>18:
    print('Vai tirar a carteira, já pode já')
elif teste == "N" or teste == "n" and idade<18:
    motorista.Dirigir(False,idade)
elif teste == "Y" or teste == "y" and idade<18:
    motorista.Dirigir(True,idade)
else:
    print('Dessa forma não dá amigo')


# Declarando um nome e mostrando suas caracteristicas
'''nome=str(input('Digite seu nome completo: '))
print('Com tamanho: {}'.format(len(nome)))
print('maiusculas: {}'.format(nome.upper()))
print('minuscuals: {}'.format(nome.lower()))
nomeSemEspaço=nome.strip().split()
nome2=nome.strip().replace(" ","")
print('Seu nome sem espaços: {}, com tamanho {} letras'.format("-".join(nomeSemEspaço),len(nome2)))
print('O seu primeiro nome tem {} letras'.format(nome.strip().find(" ")))'''