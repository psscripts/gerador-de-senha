from random import randint
from time import sleep

print('###################################')
print('#########GERADOR DE SENHAS#########')
print('###################################')

while True:
	se=int(input('\033[33mVoce quer gerar uma senha aleatoria, DIGITE 1: '))
	if se == 1:
		sleep(1)
	
		ger=randint(0,50)
		ger1=randint(50,150)
		ger2=randint(0,5)
		ger3=randint(50,5000)
		ger4=randint(500,700)
		ger5=randint(100,200)
	
		print('\033[36mGerando uma senha somente com numeros!')
		sleep(2)
    
		print('\033[35mSenha pronta')
	
		print(ger,ger1,ger3,ger4,ger5)
		print('\033[35m############')
	
	
	else:
		print('O PROGRAMA ACABOU! VOLTE SEMPRE')
		break
		
		
		
		
		
#esse script foi feito so para terbuma base de uma senha,ja que esse codigo não é nada profissional! mais sim,pode ajidqr muito gerando senhas com numeros aleatoriamente!
#alisonprogramador