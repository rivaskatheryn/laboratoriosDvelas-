"""Caderno de candidaturas da DevElas, no terminal. 

 

Rode com:  python caderno.py 

""" 

from candidaturas import ( 

    excluir_candidatura, 

    ja_se_candidatou, 

    ler_candidaturas, 

    salvar_candidatura, 

) 

from ferramentas import buscar_vaga, compatibilidade, resumo_vaga 

from vagas_lab import VAGAS 

 

MINHAS_SKILLS = ["Python", "Git", "HTML"]  # troque pelas suas skills 

 

 

def mostrar_vagas(): 

    """Mostra as vagas com a sua compatibilidade (já vem pronta).""" 

    print("\nVagas abertas:") 

    for vaga in VAGAS: 

        nota = compatibilidade(vaga, MINHAS_SKILLS) 

        print(f"  [{vaga['id']}] {resumo_vaga(vaga)}: {nota}% de compatibilidade") 

 

 


def candidatar():
    """Missão 10: pergunta o nome e o id da vaga e salva a candidatura."""

    nome = input("Seu nome: ")
    vaga_id = int(input("Id da vaga: "))

    vaga = buscar_vaga(VAGAS, vaga_id)

    if vaga is None:
        print("Vaga não encontrada.")
        return

    if ja_se_candidatou(nome, vaga_id):
        print("Você já se candidatou a essa vaga!")
        return

    salvar_candidatura(nome, vaga_id)

    print(f"Candidatura enviada para {vaga['titulo']}. Boa sorte, {nome}!")


 

 


def mostrar_candidaturas():
    """Mostra cada candidatura com o título da vaga."""

    candidaturas = ler_candidaturas()

    if not candidaturas:
        print("Nenhuma candidatura ainda.")
        return

    for candidatura in candidaturas:
        vaga = buscar_vaga(VAGAS, candidatura["vaga_id"])

        if vaga:
            print(f'{candidatura["nome"]} -> {vaga["titulo"]}')

 

 



def excluir():
    """Exclui uma candidatura."""

    nome = input("Seu nome: ")
    vaga_id = int(input("Id da vaga: "))

    apagou = excluir_candidatura(nome, vaga_id)

    if apagou:
        print("Candidatura excluída com sucesso!")
    else:
        print("Candidatura não encontrada.")



 

def menu(): 

    while True: 

        print("\n=== Caderno de candidaturas DevElas ===") 

        print("1 - Ver vagas") 

        print("2 - Me candidatar") 

        print("3 - Ver candidaturas") 

        print("4 - Excluir candidatura") 

        print("0 - Sair") 

        opcao = input("Escolha uma opção: ") 

        if opcao == "1": 

            mostrar_vagas() 

        elif opcao == "2": 

            candidatar() 

        elif opcao == "3": 

            mostrar_candidaturas() 

        elif opcao == "4": 

            excluir() 

        elif opcao == "0": 

            print("Caderno fechado. Tudo salvo no candidaturas.txt.") 

            break 

        else: 

            print("Opção inválida. Escolha um número do menu.") 

 

 

menu() 