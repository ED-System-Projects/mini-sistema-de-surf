from surfista import Surfista
from campeonato import Campeonato
from pais import Pais
from prancha import Prancha
from praia import Praia

todos_surfistas = []
todos_campeonatos = []
todos_paises = []
todas_pranchas = []
todas_praias = []

def criar_surfistas():
  nomes = ["John", "Carl", "Susan", "Mary", "Austin", "Max", "Lewis", "Braum", "Liza", "Sandy"]
  idades = [21, 22, 23, 24, 25, 34, 35, 36, 37, 40]

  for i in range(0, len(nomes)):
    novo_surfista = Surfista(nomes[i], idades[i])
    todos_surfistas.append(novo_surfista)

def criar_campeonatos():
  nomes = ["Campeonato 2015", "Campeonato 2016", "Campeonato 2017", "Campeonato 2018", "Campeonato 2019", "Campeonato 2020", "Campeonato 2021"]
  premios = [15000, 19000, 32000, 45000, 66000, 32000, 17000]

  for i in range(0, len(nomes)):
    novo_campeonato = Campeonato(nomes[i], premios[i])
    todos_campeonatos.append(novo_campeonato)

def criar_paises():
  nomes = ["Brasil", "Austrália", "EUA", "Portugal", "Indonésia"]
  linguas = ["Português", "Inglês", "Inglês", "Português", "Indonésio"]

  for i in range(0, len(nomes)):
    novo_pais = Pais(nomes[i], linguas[i])
    todos_paises.append(novo_pais)

def criar_pranchas():
  marcas = ["Marca 1", "Marca 2", "Marca 3", "Marca 4", "Marca 5", "Marca 6", "Marca 7", "Marca 8", "Marca 9", "Marca 10", "Marca 11", "Marca 6", "Marca 1", "Marca 1", "Marca 3"]
  comprimentos = [2, 2, 2.15, 1.90, 2, 2, 2, 2, 2, 2, 1.85, 2.05, 2.20, 2, 2]
  cores = ["Branco", "Azul", "Azul", "Azul", "Azul", "Vermelho", "Vermelho", "Vermelho", "Verde", "Verde", "Rosa", "Cinza", "Verde", "Marrom", "Laranja"]
  valores = [235, 137.90, 456.25, 330, 219, 456, 456.25, 456.25, 100, 917, 560, 222, 222, 417, 318]

  for i in range(0, len(marcas)):
    nova_prancha = Prancha(marcas[i], comprimentos[i], cores[i], valores[i])
    todas_pranchas.append(nova_prancha)

def criar_praias():
  nomes = ["Tambaú", "Coqueirinho", "Bessa", "Ponta de Campina", "Cabo Branco", "Teste 1", "Teste 2"]

  for i in range(0, len(nomes)):
    nova_praia = Praia(nomes[i])
    todas_praias.append(nova_praia)

def main():
  print("Bem-vindo ao sistema de surf")
  criar_surfistas()
  criar_praias()
  criar_campeonatos()
  criar_paises()
  criar_pranchas()
  #criando os relacionamentos
  #surfistas
  todos_surfistas[0].set_pranchas(todas_pranchas[0:1])
  todos_surfistas[1].set_pranchas(todas_pranchas[1:3])   #2
  todos_surfistas[2].set_pranchas(todas_pranchas[3:4])
  todos_surfistas[3].set_pranchas(todas_pranchas[4:5])
  todos_surfistas[4].set_pranchas(todas_pranchas[5:8])   #3
  todos_surfistas[5].set_pranchas(todas_pranchas[8:9])
  todos_surfistas[6].set_pranchas(todas_pranchas[9:10])
  todos_surfistas[7].set_pranchas(todas_pranchas[10:11])
  todos_surfistas[8].set_pranchas(todas_pranchas[11:12])
  todos_surfistas[9].set_pranchas(todas_pranchas[12:15])   #3

  #campeonato 
  todos_campeonatos[0].add_participante(todos_surfistas[0])
  todos_campeonatos[0].add_participante(todos_surfistas[1])
  todos_campeonatos[0].add_participante(todos_surfistas[2])
  todos_campeonatos[0].add_participante(todos_surfistas[3])
  todos_campeonatos[0].add_participante(todos_surfistas[5])
  todos_campeonatos[0].add_participante(todos_surfistas[7])
  todos_campeonatos[0].add_participante(todos_surfistas[8])
  todos_campeonatos[0].add_participante(todos_surfistas[9])
  todos_campeonatos[0].set_praia(todas_praias[0])
  todos_campeonatos[0].set_campeao(todos_surfistas[7])

  todos_campeonatos[1].add_participante(todos_surfistas[2])
  todos_campeonatos[1].add_participante(todos_surfistas[3])
  todos_campeonatos[1].add_participante(todos_surfistas[4])
  todos_campeonatos[1].add_participante(todos_surfistas[5])
  todos_campeonatos[1].add_participante(todos_surfistas[6])
  todos_campeonatos[1].add_participante(todos_surfistas[7])
  todos_campeonatos[1].add_participante(todos_surfistas[8])
  todos_campeonatos[1].set_praia(todas_praias[1])
  todos_campeonatos[1].set_campeao(todos_surfistas[2])

  todos_campeonatos[2].add_participante(todos_surfistas[3])
  todos_campeonatos[2].add_participante(todos_surfistas[4])
  todos_campeonatos[2].add_participante(todos_surfistas[5])
  todos_campeonatos[2].set_praia(todas_praias[2])
  todos_campeonatos[2].set_campeao(todos_surfistas[4])

  todos_campeonatos[3].add_participante(todos_surfistas[0])
  todos_campeonatos[3].add_participante(todos_surfistas[1])
  todos_campeonatos[3].add_participante(todos_surfistas[2])
  todos_campeonatos[3].add_participante(todos_surfistas[3])
  todos_campeonatos[3].add_participante(todos_surfistas[4])
  todos_campeonatos[3].add_participante(todos_surfistas[5])
  todos_campeonatos[3].add_participante(todos_surfistas[6])
  todos_campeonatos[3].add_participante(todos_surfistas[7])
  todos_campeonatos[3].add_participante(todos_surfistas[8])
  todos_campeonatos[3].add_participante(todos_surfistas[9])
  todos_campeonatos[3].set_praia(todas_praias[3])
  todos_campeonatos[3].set_campeao(todos_surfistas[2])

  todos_campeonatos[4].add_participante(todos_surfistas[5])
  todos_campeonatos[4].add_participante(todos_surfistas[6])
  todos_campeonatos[4].add_participante(todos_surfistas[7])
  todos_campeonatos[4].add_participante(todos_surfistas[8])
  todos_campeonatos[4].add_participante(todos_surfistas[9])
  todos_campeonatos[4].set_praia(todas_praias[4])
  todos_campeonatos[4].set_campeao(todos_surfistas[5])

  todos_campeonatos[5].add_participante(todos_surfistas[3])
  todos_campeonatos[5].add_participante(todos_surfistas[4])
  todos_campeonatos[5].add_participante(todos_surfistas[5])
  todos_campeonatos[5].set_praia(todas_praias[0])
  todos_campeonatos[5].set_campeao(todos_surfistas[5])

  todos_campeonatos[6].add_participante(todos_surfistas[3])
  todos_campeonatos[6].add_participante(todos_surfistas[4])
  todos_campeonatos[6].add_participante(todos_surfistas[5])
  todos_campeonatos[6].set_praia(todas_praias[4])
  todos_campeonatos[6].set_campeao(todos_surfistas[3])

  #países
  todos_paises[0].adicionar_praia(todas_praias[0])
  todos_paises[1].adicionar_praia(todas_praias[1])
  todos_paises[2].adicionar_praia(todas_praias[2])
  todos_paises[3].adicionar_praia(todas_praias[3])
  todos_paises[4].adicionar_praia(todas_praias[4])
  todos_paises[4].adicionar_praia(todas_praias[5])
  todos_paises[4].adicionar_praia(todas_praias[6])

  #pranchas
  todas_pranchas[0].set_fabricacao(todos_paises[3])
  todas_pranchas[1].set_fabricacao(todos_paises[0])
  todas_pranchas[2].set_fabricacao(todos_paises[1])
  todas_pranchas[3].set_fabricacao(todos_paises[3])
  todas_pranchas[4].set_fabricacao(todos_paises[3])
  todas_pranchas[5].set_fabricacao(todos_paises[4])
  todas_pranchas[6].set_fabricacao(todos_paises[4])
  todas_pranchas[7].set_fabricacao(todos_paises[2])
  todas_pranchas[8].set_fabricacao(todos_paises[0])
  todas_pranchas[9].set_fabricacao(todos_paises[4])
  todas_pranchas[10].set_fabricacao(todos_paises[1])
  todas_pranchas[11].set_fabricacao(todos_paises[2])
  todas_pranchas[12].set_fabricacao(todos_paises[3])
  todas_pranchas[13].set_fabricacao(todos_paises[3])
  todas_pranchas[14].set_fabricacao(todos_paises[0])

  #menu

  print("Seja bem-vindo ao sistema de surf! Escolha uma das opções abaixo:")
  while True:
    print("[1] Consultar praias mais selecionadas")
    print("[2] Consultar maior e menor idades dos participantes de um campeonato por surfista campeão")
    print("[3] Consultar total ganho por um surfista em todos os campeonatos que participou")
    print("[4] Consultar nomes dos surfistas que participaram de um determinado campeonato")
    print("[5] Total gasto com pranchas por surfista")
    print("[6] Total de pranchas fabricadas por um determinado país")
    print("[X] Sair")
    opcao_escolhida = input("")

    if opcao_escolhida == "1":
      quantidade_escolhida = int(input("Digite a quantidade mínima de campeonatos realizados:"))
      praias_mais_selecionadas = []
      for pais in todos_paises:
        praias_mais_selecionadas_do_pais = pais.praias_mais_selecionadas(quantidade_escolhida)
        if len(praias_mais_selecionadas_do_pais) > 0:
          praias_mais_selecionadas.extend(praias_mais_selecionadas_do_pais)
      print(f"As praias mais selecionadas de acordo com a quantidade {quantidade_escolhida} são:")
      for praia_mais_selecionada in praias_mais_selecionadas:
        print(f"{praia_mais_selecionada}")
    elif opcao_escolhida == "2":
      nome_surfista = input("Digite o nome do surfista campeão:")
      campeonatos_ganhos_por_surfista = []
      for campeonato in todos_campeonatos:
        if campeonato.get_campeao().get_nome() == nome_surfista:
          campeonatos_ganhos_por_surfista.append(campeonato)
      if len(campeonatos_ganhos_por_surfista) > 0:
        for campeonato in campeonatos_ganhos_por_surfista:
          print(f"Campeonato: {campeonato}")
          print(f"Maior idade dos participantes: {campeonato.maior_idade()}")
          print(f"Menor idade dos participantes: {campeonato.menor_idade()}")
      else:
        print("Esse surfista não existe ou não ganhou um campeonato")
    elif opcao_escolhida == "3":
      nome_surfista = input("Digite o nome do surfista:")
      surfista_encontrado = None
      for surfista in todos_surfistas:
        if surfista.get_nome() == nome_surfista:
          surfista_encontrado = surfista

      if (surfista_encontrado != None):
        campeonatos_ganhos_por_surfista = []
        for campeonato in todos_campeonatos:
          if campeonato.get_campeao() == surfista_encontrado:
            campeonatos_ganhos_por_surfista.append(campeonato)
        total_ganho = 0
        for campeonato_ganho in campeonatos_ganhos_por_surfista:
          total_ganho += campeonato_ganho.get_premio()
        print(f"O surfista {nome_surfista} ganhou o total de R$ {total_ganho} somando todos os campeonatos que participou")
      else:
        print(f"O surfista {nome_surfista} não foi encontrado")          
    elif opcao_escolhida == "4":
      nome_campeonato = input("Digite o nome do campeonato:")
      campeonato_encontrado = None
      for campeonato in todos_campeonatos:
        if campeonato.get_nome_campeonato() == nome_campeonato:
          campeonato_encontrado = campeonato
      if (campeonato_encontrado != None):
        print(f"A lista dos surfistas participantes do campeonato {campeonato_encontrado.get_nome_campeonato()}:")
        campeonato_encontrado.imprime_surfistas()
      else:
        print(f"O campeonato {nome_campeonato} não foi encontrado")
    elif opcao_escolhida == "5":
      nome_surfista = input("Digite o nome do surfista:")
      surfista_encontrado = None
      for surfista in todos_surfistas:
        if surfista.get_nome() == nome_surfista:
          surfista_encontrado = surfista

      if (surfista_encontrado != None):
        total_gasto = 0
        for prancha in surfista_encontrado.get_pranchas():
          total_gasto += prancha.get_valor()
        print(f"O surfista {nome_surfista} gastou o total de R$ {total_gasto} com pranchas")
      else:
        print(f"O surfista {nome_surfista} não foi encontrado")    
    elif opcao_escolhida == "6":
      nome_pais = input("Digite o nome do país:")
      pais_encontrado = None
      for pais in todos_paises:
        if pais.get_nome_pais() == nome_pais:
          pais_encontrado = pais
      if (pais_encontrado != None):
        quantidade_pranchas_do_pais_escolhido = 0
        for prancha in todas_pranchas:
          if prancha.get_fabricacao() == pais_encontrado:
            quantidade_pranchas_do_pais_escolhido += 1
        print(f"A quantidade de pranchas fabricadas pelo país {nome_pais} foi {quantidade_pranchas_do_pais_escolhido}")
      else:
        print(f"O país {nome_pais} não foi encontrado")
    else:
      break

  '''for i in range(0, len(todos_surfistas)):
    todos_surfistas[i].campeonatos()
    print('------------------')'''

if __name__ == "__main__":
  main()