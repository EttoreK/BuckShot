import time
import os
import random
import math

os.system("cls" if os.name == "nt" else "clear")

titulo = str(
    "\n\n"
    + "▀█████████▄  ███    █▄   ▄████████   ▄█   ▄█▄   ▄████████    ▄█    █▄     ▄██████▄      ███    \t\t   ▄████████  ▄██████▄  ███    █▄   ▄█        ▄████████     ███         ███       ▄████████\n"
    + "  ███    ███ ███    ███ ███    ███  ███ ▄███▀  ███    ███   ███    ███   ███    ███ ▀█████████▄\t\t  ███    ███ ███    ███ ███    ███ ███       ███    ███ ▀█████████▄ ▀█████████▄  ███    ███\n"
    + "  ███    ███ ███    ███ ███    █▀   ███▐██▀    ███    █▀    ███    ███   ███    ███    ▀███▀▀██\t\t  ███    ███ ███    ███ ███    ███ ███       ███    █▀     ▀███▀▀██    ▀███▀▀██  ███    █▀ \n"
    + " ▄███▄▄▄██▀  ███    ███ ███        ▄█████▀     ███         ▄███▄▄▄▄███▄▄ ███    ███     ███   ▀\t\t ▄███▄▄▄▄██▀ ███    ███ ███    ███ ███      ▄███▄▄▄         ███   ▀     ███   ▀ ▄███▄▄▄    \n"
    + "▀▀███▀▀▀██▄  ███    ███ ███       ▀▀█████▄   ▀███████████ ▀▀███▀▀▀▀███▀  ███    ███     ███    \t\t▀▀██████▀▀   ███    ███ ███    ███ ███      ▀███▀▀▀         ███         ███    ▀▀███▀▀▀    \n"
    + "  ███    ██▄ ███    ███ ███    █▄   ███▐██▄           ███   ███    ███   ███    ███     ███    \t\t▀████▀███▄   ███    ███ ███    ███ ███       ███    █▄      ███         ███      ███    █▄ \n"
    + "  ███    ███ ███    ███ ███    ███  ███ ▀███▄   ▄█    ███   ███    ███   ███    ███     ███    \t\t  ███  ▀███▄ ███    ███ ███    ███ ███▌    ▄ ███    ███     ███         ███      ███    ███\n"
    + "▄█████████▀  ████████▀  ████████▀   ███   ▀█▀ ▄████████▀    ███    █▀     ▀██████▀     ▄████▀  \t\t  ███    ▀██  ▀██████▀  ████████▀  █████▄▄██ ██████████    ▄████▀      ▄████▀    ██████████\n\n"
    + "\t\t\t     ▄█  ▄██████▄     ▄██████▄     ▄████████    ▄████████\t\t\t\t\t   ▄████████    ▄████████  ▄█     ▄████████\n"
    + "\t\t\t    ▐██ ███    ███   ███    ███   ███    ███   ███    ███\t\t\t\t\t  ███    ███   ███    ███ ███    ███    ███\n"
    + "\t\t\t    ▐██ ███    ███   ███    █▀    ███    ███   ███    ███\t\t\t\t\t  ███    █▀    ███    ███ ███▌   ███    ███\n"
    + "\t\t\t    ▐██ ███    ███  ▄███          ███    ███  ▄███▄▄▄▄██▀\t\t\t\t\t  ███          ███    ███ ███▌  ▄███▄▄▄▄██▀\n"
    + "\t\t\t    ▐██ ███    ███ ▀▀███ ████▄  ▀███████████ ▀▀██████▀▀  \t\t\t\t\t▀███████████ ▀███████████ ███▌ ▀▀██████▀▀  \n"
    + "\t\t\t▄   ▐██ ███    ███   ███    ███   ███    ███ ▀████▀███▄  \t\t\t\t\t         ███   ███    ███ ███  ▀████▀███▄  \n"
    + "\t\t\t██  ▐█▀ ███    ███   ███    ███   ███    ███   ███  ▀███▄\t\t\t\t\t   ▄█    ███   ███    ███ ███    ███  ▀███▄\n"
    + "\t\t\t ▀███▀   ▀██████▀    ████████▀    ███    █▀    ███    ▀██\t\t\t\t\t ▄████████▀    ███    █▀  █▀     ███    ▀██"
    + "\n\n"
)
dict_itens = { 0: "detector", 1: "biblia", 2: "pilula", 3: "anzol", 4: "alvo", 5: "algema", 6: "polvora"}
tempo_ocioso = 0.5
vez = {0: 0, 1: 0}

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):

  if (curDepth == targetDepth):
      return scores[nodeIndex]
  
  if (maxTurn):
      return max(minimax(curDepth + 1, nodeIndex * 2,
      False, scores, targetDepth),
      minimax(curDepth + 1, nodeIndex * 2 + 1,
      False, scores, targetDepth))
  else:
      return min(minimax(curDepth + 1, nodeIndex * 2,
      True, scores, targetDepth),
      minimax(curDepth + 1, nodeIndex * 2 + 1,
      True, scores, targetDepth))

def nivel(rodada):
    match rodada:
        case 0:
            vida = random.randint(2, 3)
            balas = random.randint(1, 3)
        case 1:
            vida = random.randint(2, 3)
            balas = random.randint(1, 4)
        case 2:
            vida = random.randint(2, 4)
            balas = random.randint(2, 4)
        case 3:
            vida = random.randint(3, 4)
            balas = random.randint(2, 5)
        case 4:
            vida = random.randint(3, 5)
            balas = random.randint(3, 5)
        case 5:
            vida = random.randint(3, 6)
            balas = random.randint(3, 6)
        case 6:
            vida = random.randint(4, 6)
            balas = random.randint(4, 7)
    fase = {
        "vida": vida,
        "balas": balas,
        "balas-vazias": 0,
        "balas-perigosas": random.randint(1, balas),
    }
    fase["balas-vazias"] = balas - fase["balas-perigosas"]
    return fase

def itens(itens):
    # 1 - detector (index de uma bala-perigosa qualquer)
    # 2 - bíblia (inverte a periculosidade da bala no gatilho)
    # 3 - pilula (recupera até 2 de vida)
    # 4 - anzol (roubar um item da IA e usar automaticamente)
    # 5 - alvo (descarta a bala no gatilho)
    # 6 - algema (pula a vez do adversario)
    # 7 - pólvora (duplica o dano)
    for i in range(3):
        if sum(itens.values()) == 5:
            print(
                "Item %s descartado, muitos itens na mesa"
                % random.choice(list(itens.keys()))
            )
        else:
            itens[str(random.choice(list(itens.keys())))] += 1

    return itens

def engatilhar(fase):
    balas = []
    balasVazias = fase["balas-vazias"]
    balasPerigosas = fase["balas-perigosas"]
    while len(balas) != (fase["balas-vazias"] + fase["balas-perigosas"]):
        var = random.choice(["balas-vazias", "balas-perigosas"])
        if var == "balas-vazias" and balasVazias != 0:
            balas.append(0)
            balasVazias -= 1
        elif var == "balas-perigosas" and balasPerigosas != 0:
            balas.append(1)
            balasPerigosas -= 1
    # print("balas: ", balas)
    return balas

def jogada(moeda, vidaIA, vidaJ, itensIA, itensJ, balas):
    dano = 1
    jogada_opcao = 0
    moeda2 = True

    if moeda:
        print("\nHumano - balas: [%s]\n\n" % str(balas)[1:-1])
        vidaM = vidaJ
        vidaI = vidaIA
        itensM = itensJ
        itensI = itensIA

        while jogada_opcao != "N" and sum(itensM.values()) > 0:

            index = 0

            ##### Mostra vidas e itens de jogador e computador
            print(
                "\t\t\tJogador [Vidas: %i]\t\t\t\t\tComputador [Vidas: %i]\n"
                % (vidaM, vidaI)
            )

            for index_item, nome_item in enumerate(itensM.keys()):
                print(
                    "\t#%i\t\t[%i] - %s\t\t\t\t\t[%i] - %s"
                    % (index_item, itensM[nome_item], nome_item, itensI[nome_item], nome_item)
                )

            jogada_opcao = input("Usar item [S|N]: ").upper()

            if jogada_opcao == "S":
                index = input("Digite o index do item: ")

                try:
                    index = int(index)
                except:
                    print("Digite apenas o index do item")

                if list(itensM.values())[index] != 0:
                    match index:
                        case 0:
                            # detector
                            detector = balas.index(1)
                            if detector != 0:
                                print("A %iª bala é perigosa" % detector)
                            else:
                                print("Não há mais nenhuma bala perigosa")
                        case 1:
                            # biblia
                            if balas[-1] == 0:
                                balas[-1] = 1
                            else:
                                balas[-1] = 0
                            print("Bala no gatilho inverteu de periculosidade")
                        case 2:
                            # pilula
                            if (fase["vida"] - vidaM) >= 3:
                                vidaM += 2
                                print("Item pilula usado, a vida aumentou em 2 pontos")
                            else:
                                vidaM += fase["vida"] - vidaM
                                print("Item pilula usado, a vida aumentou em 1 ponto")
                        case 3:
                            # anzol
                            index = input("Digite o index do item para roubar: ")

                            try:
                                index = int(index)
                            except:
                                print("Digite apenas o index do item")

                            if list(itensM.values())[index] == 0:
                                print("Nenhum item roubado, gastou o item")
                            else:
                                print("Item %s roubado" % list(itensM)[index])
                                itensM[dict_itens[index]] += 1
                                itensI[dict_itens[index]] -= 1
                        case 4:
                            # alvo
                            if len(balas):
                                balas.pop()
                        case 5:
                            # algema
                            moeda2 = not moeda2
                            print("item algema usado, agora a troca de vez é: ", moeda2)
                        case 6:
                            # polvora
                            if dano == 1:
                                dano = 2
                            print("item polvora usado, agora o dano da bala é: ", dano)

                    itensM[dict_itens[index]] -= 1
                else:
                    print("Você não possui este item")

            elif jogada_opcao != "N" and jogada_opcao != "S":
                print('Digite "S" ou "N" para depois escolher o item')
            
            vidaI -= balas.pop(-1) * dano

            vidaJ = vidaM
            vidaIA = vidaI
            itensJ = itensM
            itensIA = itensI
    
    else:
        print("\nPC jogando - balas: [%s]\n\n" % str(balas)[1:-1])
        vidaM = vidaIA
        vidaI = vidaJ
        itensM = itensIA
        itensI = itensJ

        print(
            "\t\t\tJogador [Vidas: %i]\t\t\t\t\tComputador [Vidas: %i]\n"
            % (vidaI, vidaM)
        )

        for index_item, nome_item in enumerate(itensM.keys()):
            print(
                "\t#%i\t\t[%i] - %s\t\t\t\t\t[%i] - %s"
                % (index_item, itensI[nome_item], nome_item, itensM[nome_item], nome_item)
            )

        pontos = [3, 5, 2, 9, 12, 5, 23, 23]
        treeDepth = math.log(len(pontos), 2)
        print("The optimal value is : ", end = "")
        print(minimax(0, 0, True, pontos, treeDepth))

        vidaI -= balas.pop(-1) * dano

        vidaIA = vidaM
        vidaJ = vidaI
        itensIA = itensM
        itensJ = itensI

    if moeda2:
        moeda = not moeda

    return (moeda, vidaIA, vidaJ, itensIA, itensJ, balas)

while True:
    print(titulo)
    opcao_inicial = input(
        'Digite "J" para jogar, "S" para sair e "T" para ver o tutorial\n'
    ).upper()

    if opcao_inicial == "J":
        time.sleep(tempo_ocioso)
        os.system("cls" if os.name == "nt" else "clear")
        rodada = -1
        vidaIA = 0
        itens_jogo = {
            "detector": 0,
            "biblia": 0,
            "pilula": 0,
            "anzol": 0,
            "alvo": 0,
            "algema": 0,
            "polvora": 0
        }

        while True:
            print("\n" + 38 * "=" + "\n\t\tRodada: ", rodada, "\n" + 38 * "=")

            if vidaIA <= 0:
                os.system("cls" if os.name == "nt" else "clear")
                rodada += 1
                fase = nivel(rodada)
                vidaIA = fase["vida"]
                vidaJ = fase["vida"]
                balas = engatilhar(fase)
                moeda = random.randint(0, 1)
                itensJ = itens(itens_jogo.copy())
                itensIA = itens(itens_jogo.copy())

            if balas == []:
                balas = engatilhar(fase)

            if 0 not in list(vez.values()):
                vez[0] = 0
                vez[1] = 0
                itensJ = itens(itensJ)
                itensIA = itens(itensIA)
            else: 
                vez[moeda] += 1

            moeda, vidaIA, vidaJ, itensIA, itensJ, balas = jogada(
                moeda, vidaIA, vidaJ, itensIA, itensJ, balas
            )

            if vidaJ <= 0:
                os.system("cls" if os.name == "nt" else "clear")
                print("perdeuuuuuu")
                time.sleep(tempo_ocioso)
                break

            if rodada >= 8:
                os.system("cls" if os.name == "nt" else "clear")
                print("Venceu, ganhou, agora acabou")
                time.sleep(tempo_ocioso)
                break
            
            time.sleep(tempo_ocioso)

    elif opcao_inicial == "S":
        print("Saindo...")
        break
    elif opcao_inicial == "S":
        os.system("cls" if os.name == "nt" else "clear")
        print("Tutorial")
        input("\nDigite qualquer tecla para voltar\n")
    else:
        print(
            'Digite "J" e aperte ENTER para começar o jogo\n'
            + 'Digite "S" e aperte ENTER para sair'
        )
        time.sleep(tempo_ocioso)

    os.system("cls" if os.name == "nt" else "clear")