import random as rd
def situacao(x):
	
	if x == 1:
		print(" 	Você já esteve caminhando por algum tempo, e por estar muito exposto ao sol por passa a sentir sede.\n")
		print(" Opção A - Inicia uma busca por água.")
		print(" Opção B - Caminha pelas redondezas, tentando reconhecer o ambiente, antes de procurar por água.")
		escolha = str(input(" \n Digite A para escolher a opção A e B para escolher a opção B.\n"))
		if escolha == 'A':
			r = rd.random()
			if r < 0.5:
				print(" 	Após alguns minutos de caminhada, você felizmente acha um rio, e consegue se hidratar.")
				r = rd.random() 
				if r < 0.7:
					print(" 	A água estava limpa, e você seguiu em frente, explorando a floresta.")
				else:
					vive = False
					print(" 	Oh não, a água estava contaminada, você se sente tonto e desmaia, animais selvagens que estavam por perto acabam te atacando, e você não teve forças para lutar por sua vida.")				
					return False
			else:
				print(" 	Você ja esteve andando por algumas horas agora, mal tem forças para sustentar seu corpo, devido a desidratação, você esta perdendo as esperanças de encontrar água. \n")
				print(" Opção A - Você bebe sua própria urina, em um momento de desespero.")
				print(" Opção B - Você continua sua procura por água.")
				resp = str(input(" \n Digite A para escolher a opção A e B para escolher a opção B.\n"))
				if resp == 'A':
					print(" \n	O sabor pode não ser dos melhores, mas pelo menos te ajuda momentaneamente, e você cria forças para andar mais um pouco.")
				if resp == 'B': 
					r = rd.random()
					if r < 0.6:
						print(" \n	Ufa, foi por pouco, mas você conseguiu achar água, se hidratar, e continuar com sua jornada.")
					else:
						vive = False
						print(" \n	 Você se mantém de pé caminhando o máximo que você aguenta, mas uma hora a falta de água iria te derrubar. Você desmaia e é atacado por alguns animais selvagens, você não resistiu.")
						return False
		if escolha == 'B':
			r = rd.random()
			if r < 0.2:
				print(" 	Você caminha pelos arredores da floresta, e não demora muito até que, por sorte, você ache um rio.")
			else:
				vive = False
				print(" 	Você caminha, tentando reconhecer o território, e está tão concentrado em não se perder que não percebe que está se desidratando. Você se sente tonto e desmaia, animais selvagens que estavam por perto acabam te atacando, e você não teve forças para lutar por sua vida.")				
				return False

	elif x == 2:
		print(" 	Você sente seu estômago roncar, já faz um tempo desde sua última refeição. \n")
		print(" Opção A - Sair para caçar. ")
		print(" Opção B - Sair para pescar. ")
		resp = str(input(" \n 	Digite A para escolher a opção A e B para escolher a opção B. \n"))
		if resp == 'A':
			r = rd.random()
			if r < 0.6:		
				print(" 	Você conseguiu encontrar um animal de pequeno porte e caça-lo, isso será suficiente para matar sua fome.")
			else:
				print(" 	Você não conseguiu achar nenhum animal pelas redondezas, mas você encontra um arbusto com frutinhos que parecem ser bem apetitosos. \n")
				print(" Opção A - Comer os frutos. ")
				print(" Opção B - Não comer os frutos.")
				resp = str(input(" \n	Digite A para escolher a opção A e B para escolher a opção B.\n"))
				if resp == 'A':
					r = rd.random()
					if r < 0.6:		
						vive = False
						print(" 	Infelizmente, você comeu uma planta envenenada, não demora muito até que suas vias aéreas se fechem por completo, e voce morre asfixiado")
						return False
					else:
						print(" 	Até que esses frutos não são tão ruins, definitivamente é um bom alimento para emergências.")
				if resp == 'B':
					vive = False
					print(" 	Comer os frutos era uma decisão arriscada já que você não conhecia a procedência deles. Você tenta continuar sua jornada, mas depois de dias não acha nenhum recurso comestível e acaba morrendo, sem nutrientes para sustentar seu corpo.")
					return False
		if resp == 'B':
			r = rd.random()
			if r < 0.6:	
				print(" 	Você encontra um lago cheio de peixes, você pesca o suficiente para se alimentar pelo dia")
			else:
				print(" 	Parece que nem existem peixes nessa região da floresta, mas você encontra um arbusto com frutinhos que parecem ser bem apetitosos.\n")
				print(" Opção A - Comer os frutos. ")
				print(" Opção B - Não comer os frutos.")
				resp = str(input(" \n	Digite A para escolher a opção A e B para escolher a opção B.\n"))
				if resp == 'A':
					r = rd.random()
					if r < 0.6:		
						vive = False
						print(" 	Infelizmente, você comeu uma planta envenenada, não demora muito até que suas vias aéreas se fechem por completo, e voce morre asfixiado")
						return False
					else:
						print(" 	Até que esses frutos não são tão ruins, definitivamente é um bom alimento para emergências.")
				if resp == 'B':
					vive = False
					print(" 	Comer os frutos era uma decisão arriscada já que você não conhecia a procedência deles. Você tenta continuar sua jornada, mas depois de dias não acha nenhum recurso comestível e acaba morrendo, sem nutrientes para sustentar seu corpo.")			
					return False
	
	elif x == 3:
		print(" 	Sem saber quanto tempo você vai ficar na floresta, você pensa que fazer uma arma para se proteger dos possíveis perigos seria interessante.\n")
		print(" Opção A - Utiliza um pedaço de madeira e tenta afiá-lo para se defender.")
		print(" Opção B - Ignora os pedaços de madeira e procura por algum material mais resistente, uma faca perdida na floresta, algo do tipo.")
		resp = str(input(" \n	Digite A para escolher a opção A e B para escolher a opção B.\n"))
		if resp == 'A':
			r = rd.random()
			if r < 0.7:	
				print("	Você conseguiu fazer uma boa arma afiando o pedaço de madeira, um animal selvagem veio te atacar, mas você conseguiu se defender.")
			else:
				vive = False
				print("	Você até tentou deixar sua arma afiada, mas não foi o suficiente para sua arma ficar boa, voce sofreu um ataque de um animal selvagem, mas não conseguiu se defender.")
				return False
		if resp == 'B':
			r = rd.random()
			if r < 0.7:
				vive = False
				print("	Você não encontrou nada que poderia usar como uma arma, um animal selvagem te atacou, e você não tinha nada para se defender, você não sobreviveu ao ataque.")
				return False
			else:
				print("	Surpreendentemente, você encontrou uma adaga perdida na floresta, ela está um pouco enferrujada, mas ira servir por enquanto, você sofreu um ataque de um animal selvagem, mas conseguiu se defender com sucesso usando sua arma.")
	
	elif x == 4:
		print(" 	Você pensa que seria interessante reconhecer melhor a área da floresta em que você está, para aproveitar ao máximo todos os recursos disponíveis. \n")
		print(" Opção A - Escalar uma árvore, para ter uma visão geral, e enxergar coisas que estão longe de você.")
		print(" Opção B - Caminhar até encontrar novos recursos, fazendo uma trilha para não se perder, e conseguir voltar ao local onde você está instalado sem grandes dificuldades.")
		resp = str(input(" \n	Digite A para escolher a opção A e B para escolher a opção B.\n"))
		if resp == 'A':
			r = rd.random()
			if r < 0.7:
				print(" 	Você consegue observar e analisar bem o que está a sua volta, certamente te ajudará a se localizar nessa floresta.")
			else:
				vive = False
				print(" 	Em um momento de distração, você perde o equilíbrio e cai da árvore, no acidente, você bate sua cabeça em uma grande pedra, e sangra até a morte.")
				return False
		if resp == 'B':
			r = rd.random()
			if r < 0.6:
				print(" 	Sua estratégia de explorar a floresta e fazer uma trilha deu certo, agora você tem uma noção melhor da área que você está e pode voltar tranquilamente quando quiser.")
			else:
				vive = False
				print(" 	Você se perde da sua trilha, e não consegue voltar para onde você estava, eventualmente seus recursos acabam, e você não consegue achar outros, causando sua morte.")
				return False
				
	elif x == 5:
		print(" 	Está anoitecendo, e o clima está esfriando, foi um dia longo, e você quer poder relaxar e descansar um pouco. \n")
		print(" Opção A - Fazer uma fogueira.")
		print(" Opção B - Não fazer uma fogueira.")
		resp = str(input("\n	 Digite A para escolher a opção A e B para escolher a opção B.\n"))
		if resp == 'A':
			r = rd.random()
			if r < 0.7:
				print(" 	Ao fazer a fogueira, você ajeita algumas folhas no chão e faz um bom colchão improvisado, você consegue descansar pela noite.")
			else:
				vive = False
				print(" 	A fogueira te deixa aquecido e relaxado, você está quase caindo no sono quando ouve barulhos estranhos, você imagina que tenham sido causados pelo vento e não se preocupa, porém eram animais selvagens que vieram te atacar, você não foi rápido suficiente para se proteger, e acaba morrendo.")
				return False
		if resp == 'B':
			r = rd.random()
			if r < 0.6:
				print(" 	Você não faz uma fogueira, e ficar atento durante a noite para previnir possíveis perigos. Em algum momento da madrugada, animais selvagens se aproximam, como você estava atento, você consegue escapar com vida de um possível ataque.")
			else:
				vive = False
				print(" 	Por estar exausto e a muitas horas sem dormir, você sofre alucinações e se assusta. Você acaba se colocando numa situação de perigo, e acaba morrendo.")
				return False
	
	elif x == 6:
		print(" 	Está anoitecendo, e o clima está esfriando, foi um dia longo, e você quer poder relaxar e descansar um pouco. \n")
		print(" Opção A - Dormir.")
		print(" Opção B - Não dormir.")
		resp = str(input(" \n	Digite A para escolher a opção A e B para escolher a opção B.\n"))
		if resp == 'A':
			r = rd.random()
			if r < 0.7:
				print(" 	Você ajeita algumas folhas no chão e faz um bom colchão impovisado, você consegue descansar, tendo uma boa noite de sono.")
			else:
				vive = False
				print(" 	Você se aconchega numa pilha de folhas, e decide dormir no local, você consegue dormir por algumas horas, até que animais selvagens que vieram te atacar, você não foi rápido suficiente para se proteger, e acaba morrendo.")
				return False
		if resp == 'B':
			r = rd.random()
			if r < 0.6:
				print(" 	Você decide não descansar e ficar atento durante a noite para previnir possíveis perigos. Em algum momento da madrugada, animais selvagens se aproximam, como você estava atento, você consegue escapar com vida de um possível ataque.")
			else:	
				vive = False
				print(" 	Por estar exausto e a muitas horas sem dormir, você sofre alucinações e se assusta. Você acaba se colocando numa situação de perigo, e acaba morrendo.")
				return False

name = str(input(" Insira aqui seu nome: "))
vive = True
continuar = True
pontos = 0	
dia = 1
ultimo_dia = 1
menor_dia = 1
maior_dia = 1
total_dia = 0
run = 1
nota = 0.0
y = 0

while continuar == True: 
	print("\n   Bom jogo,", name, ":)\n")
	while vive == True:
		print(" ===== Dia " ,dia,"===== \n")
		sit = rd.randint(1,4)
		x = sit
		vive = situacao(sit)
		if vive == False:
			print(" \n Você completou",run,"runs.")
			valor = str(input(" \n Dê uma nota para esta rodada de -5 a 5 (valores podem ser decimais) \n" ))
			nota = nota + float(valor)
			print(" \n ===== Você Morreu - Volte ao Dia 1 =====\n ")
			break
		print(" \n ----------------------------------------------------- \n")

		sit = rd.randint(1,4)
		while sit == x:
			sit = rd.randint(1,4)
		vive = situacao(sit)
		if vive == False:
			print(" \n Você completou",run,"runs.")
			valor = str(input(" \n Dê uma nota para esta rodada de -5 a 5 (valores podem ser decimais) \n" ))
			nota = nota + float(valor)
			print(" \n ===== Você Morreu - Volte ao Dia 1 =====\n ")
			break
		print(" \n ----------------------------------------------------- \n")

		print(" ===== Noite " ,dia,"===== \n ")

		sit = rd.randint(5,6)
		vive = situacao(sit)
		if vive == False:
			print(" \n Você completou",run,"runs.")
			valor = str(input(" \n Dê uma nota para esta rodada de -5 a 5 (valores podem ser decimais) \n" ))
			nota = nota + float(valor)
			print(" \n ===== Você Morreu - Volte ao Dia 1 =====\n ")
			break
		print(" \n ----------------------------------------------------- \n")
		
		valor = str(input(" \n Dê uma nota para esta rodada de -5 a 5 (valores podem ser decimais) \n" ))
		print(" \n ===================================================== \n ")
		nota = nota + float(valor)
		dia = dia + 1
		vive = True

	print(" ============================================================ ")
	print(" \n Você deseja continuar sonhando?\n" )
	print(" Digite A, para sim. ")
	print(" Digite B, para não. ")
	resp = str(input(" \n	Escolha entre A e B. \n"))
	if resp == 'A':
		continuar = True
		vive = True
		if menor_dia < dia:
			menor_dia = menor_dia
		elif ultimo_dia < dia:
			maior_dia = dia
		total_dia = total_dia + dia
		ultimo_dia = dia
		dia = 1
		run = run + 1
	if resp == 'B':
		continuar = False
		total_dia = total_dia + dia
		if ultimo_dia <= dia:
			menor_dia = ultimo_dia
			maior_dia = dia
		else:
			maior_dia = ultimo_dia
			ultimo_dia = dia
		print("\n Estatísticas de",name,":")
		print("\n Runs: ",run)
		print(" Maior número de Dias por Run: ",maior_dia)
		print(" Menor número de Dias por Run: ",menor_dia)
		print(" Média de número de Dias por Run: ",total_dia/run)
		print(" Nota final para o jogo: ",nota)
		
		print("\n Obrigado por Jogar!!! :)")
