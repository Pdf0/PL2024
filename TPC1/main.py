
import sys

def parse(fpath):
    with open(fpath) as f:
        list = []
        lines = f.readlines()
        keys = lines[0].rstrip().split(',')
        for line in lines[1:]:
            values = line.rstrip().split(',')
            list.append(dict(zip(keys, values)))  
    return list          

def menu():
    print("\n----- PL2024 - TPC1 -----\n")
    print("1) Listar modalidades por ordem alfabética")
    print("2) Percentagens de atletas aptos e inaptos para a prática desportiva")
    print("3) Distribuição de atletas por escalão etário")
    return input("Escolhe uma opção: ")

def qOne(data):
    modalidades = sorted(list(set([i['modalidade'] for i in data])))
    print("\nModalidades existentes:")
    for m in modalidades:
        print(f"-> {m}")
    

def qTwo(data):
    total = len(data)
    aptos = len([i for i in data if i['resultado'] == 'true'])
    inaptos = len([i for i in data if i['resultado'] != 'true'])
    print("\nPercentagens de atletas aptos e inaptos para a prática desportiva")
    print(f"Total de Atletas: {total}\nAtletas Aptos: {aptos} - {round((aptos/total)*100, 2)}%\nAtletas Inaptos: {inaptos} - {round((inaptos/total)*100, 2)}%")

def qThree(data):
    escaloes = {}
    total = len(data)
    for p in data:
        idade = int(p['idade'])
        escalao = (idade // 5) * 5
        if escalao not in escaloes:
            escaloes[escalao] = 0
        escaloes[escalao] += 1
    
    print("\nDistribuição de Atletas por Escalão Etário:")
    print(f"Total de atletas: {total}")
    for escalao, count in sorted(escaloes.items()):
        print(f"{escalao}-{escalao + 4} anos: {count} - {round((count/total)*100, 2)}%")

def main(args):

    if len(args) != 2:
        print("Insere só um ficheiro como argumento")
        exit(1)
    
    data = parse(args[1])

    while True:
        option = menu()
        if option == '1':
            qOne(data)
        elif option == '2':
            qTwo(data)
        elif option == '3':
            qThree(data)
        else:
            print('Opção Inválida')

if __name__ == "__main__":
    main(sys.argv)