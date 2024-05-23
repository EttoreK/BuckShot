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
dict_itens = {
    0: "Detector",
    1: "Biblia",
    2: "Pilula",
    3: "Anzol",
    4: "Alvo",
    5: "Algema",
    6: "Polvora"
}
tempo_ocioso = 0.5
vez = {0: 0, 1: 0}

def minimax(cur_depth, node_index, max_turn, scores, target_depth):
    if cur_depth == target_depth:
        return scores[node_index]

    if max_turn:
        return max(
            minimax(cur_depth + 1, node_index * 2, False, scores, target_depth),
            minimax(cur_depth + 1, node_index * 2 + 1, False, scores, target_depth),
        )
    else:
        return min(
            minimax(cur_depth + 1, node_index * 2, True, scores, target_depth),
            minimax(cur_depth + 1, node_index * 2 + 1, True, scores, target_depth),
        )

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
    balas_vazias = fase["balas-vazias"]
    balas_perigosas = fase["balas-perigosas"]
    while len(balas) != (fase["balas-vazias"] + fase["balas-perigosas"]):
        var = random.choice(["balas-vazias", "balas-perigosas"])
        if var == "balas-vazias" and balas_vazias != 0:
            balas.append(0)
            balas_vazias -= 1
        elif var == "balas-perigosas" and balas_perigosas != 0:
            balas.append(1)
            balas_perigosas -= 1
    # print("balas: ", balas)
    return balas

def jogada(moeda, vida_ia, vida_j, itens_ia, itens_j, balas):
    dano = 1
    jogada_opcao = 0
    moeda2 = True

    if moeda:
        print("\nHumano - balas: [%s]\n\n" % str(balas)[1:-1])
        vida_m = vida_j
        vida_i = vida_ia
        itens_m = itens_j
        itens_i = itens_ia

        while jogada_opcao != "N" and sum(itens_m.values()) > 0:

            index = 0

        # Mostra vidas e itens de jogador e computador
            print(
                "\t\t\tJogador [Vidas: %i]\t\t\t\t\tComputador [Vidas: %i]\n"
                % (vida_m, vida_i)
            )

            for index_item, nome_item in enumerate(itens_m.keys()):
                print(
                    "\t#%i\t\t[%i] - %s\t\t\t\t\t[%i] - %s"
                    % (
                        index_item,
                        itens_m[nome_item],
                        nome_item,
                        itens_i[nome_item],
                        nome_item
                    )
                )

            jogada_opcao = input("Usar item [S|N]: ").upper()

            if jogada_opcao == "S":
                index = input("Digite o index do item: ")

                try:
                    index = int(index)
                except ValueError:
                    print("Digite apenas o index do item")

                if index in dict_itens and list(itens_m.values())[index] != 0:
                    match index:
                        case 0:
                            # detector
                            try:    
                                detector = balas.reverse().index(1)
                                print("A %iª bala é perigosa" % (detector + 1))
                            except:
                                print("Nenhuma bala perigosa na arma")
                        case 1:
                            # biblia
                            try:
                                if balas[-1] == 0:
                                    balas[-1] = 1
                                else:
                                    balas[-1] = 0
                                print("Bala no gatilho inverteu de periculosidade")
                            except:
                                print("As balas fugiram")
                        case 2:
                            # pilula
                            if (fase["vida"] - vida_m) >= 2:
                                vida_m += 2
                                print("Item pilula usado, a vida aumentou em 2 pontos")
                            elif (fase["vida"] == vida_m):
                                vida_m += 0 
                            else:
                                vida_m += 1
                                print("Item pilula usado, a vida aumentou em 1 ponto")
                        case 3:
                            # anzol
                            index_item = input("Digite o index do item para roubar: ")

                            try:
                                index_item = int(index_item)
                            except ValueError:
                                print("Digite apenas o index do item")
                                next

                            if list(itens_i.values())[index_item] == 0:
                                print("Nenhum item roubado, gastou o item")
                            else:
                                itens_m[dict_itens[index_item]] += 1
                                itens_i[dict_itens[index_item]] -= 1
                                print("Item %s roubado" % list(itens_m)[index_item])
                        case 4:
                            # alvo
                            try:
                                balas.pop()
                                print("item alvo usado, agora", "tem [%i] no cartucho" % len(balas) if len(balas) else "não tem balas no cartucho")
                            except:
                                balas
                                print("Não tinha nenhuma bala no cartucho, gastou o item")
                        case 5:
                            # algema
                            if moeda2:
                                moeda2 = not moeda2
                            print("item algema usado, turno adversário pulado")
                        case 6:
                            # polvora
                            dano = 2
                            print("item polvora usado, agora o dano da bala é: ", dano)

                    itens_m[dict_itens[index]] -= 1
                else:
                    print("Você não possui este item")

            elif jogada_opcao != "N" and jogada_opcao != "S":
                print('Digite "S" ou "N" para depois escolher o item')
            
        try:
            vida_i -= balas.pop(-1) * dano
        except:
            print("Cartucho vazio")

        vida_j = vida_m
        vida_ia = vida_i
        itens_j = itens_m
        itens_ia = itens_i
        
    else:
        index = 0

        print("\nMAQUINA - balas: [%s]\n\n" % str(balas)[1:-1])
        vida_m = vida_ia
        vida_i = vida_j
        itens_m = itens_ia
        itens_i = itens_j

        print(
            "\t\t\tJogador [Vidas: %i]\t\t\t\t\tComputador [Vidas: %i]\n"
            % (vida_i, vida_m)
        )

        for index_item, nome_item in enumerate(itens_m.keys()):
            print(
                    "\t#%i\t\t[%i] - %s\t\t\t\t\t[%i] - %s"
                    % (
                        index_item,
                        itens_i[nome_item],
                        nome_item,
                        itens_m[nome_item],
                        nome_item
                    )
                )
            
        pontos = [3, 5, 2, 9, 12, 5, 23, 23]
        tree_depth = math.log(len(pontos), 2)
        print("The optimal value is : ", end="")
        print(minimax(0, 0, True, pontos, tree_depth))

        itens_m[dict_itens[index]] -= 1
            
        try:
            vida_i -= balas.pop(-1) * dano
        except:
            print("Cartucho vazio")

        vida_ia = vida_m
        vida_j = vida_i
        itens_ia = itens_m
        itens_j = itens_i

    if moeda2:
        moeda = not moeda

    return (moeda, vida_ia, vida_j, itens_ia.copy(), itens_j.copy(), balas)

while True:
    print(titulo)
    opcao_inicial = input(
        'Digite "J" para jogar, "S" para sair e "T" para ver o tutorial\n'
    ).upper()

    if opcao_inicial == "J":
        time.sleep(tempo_ocioso)
        os.system("cls" if os.name == "nt" else "clear")
        rodada = -1
        vida_ia = 0
        itens_jogo = {
            "Detector": 0,
            "Biblia": 0,
            "Pilula": 0,
            "Anzol": 0,
            "Alvo": 0,
            "Algema": 0,
            "Polvora": 0
        }

        while True:
            print("\n" + 38 * "=" + "\n\t\tRodada: ", rodada, "\n" + 38 * "=")

            if vida_ia <= 0:
                os.system("cls" if os.name == "nt" else "clear")
                rodada += 1
                fase = nivel(rodada)
                vida_ia = fase["vida"]
                vida_j = fase["vida"]
                balas = engatilhar(fase)
                moeda = random.randint(0, 1)
                itens_j = itens(itens_jogo.copy())
                itens_ia = itens(itens_jogo.copy())

            if balas == []:
                balas = engatilhar(fase)

            if 0 not in list(vez.values()):
                vez[0] = 0
                vez[1] = 0
                itens_j = itens(itens_j)
                itens_ia = itens(itens_ia)
            else:
                vez[moeda] += 1

            moeda, vida_ia, vida_j, itens_ia, itens_j, balas = jogada(
                moeda, vida_ia, vida_j, itens_ia, itens_j, balas
            )

            if vida_j <= 0:
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