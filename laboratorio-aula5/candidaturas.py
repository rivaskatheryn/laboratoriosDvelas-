"""Caderno de candidaturas: guarda, lê e apaga candidaturas num arquivo de texto. 

 

Cada linha do arquivo é uma candidatura, no formato  nome;id_da_vaga 

Exemplo de linha:  Ana Souza;2 

""" 

import os 

 

# O arquivo fica sempre na pasta do laboratório, de onde quer que o programa rode 

PASTA = os.path.dirname(os.path.abspath(__file__)) 

ARQUIVO = os.path.join(PASTA, "candidaturas.txt") 

 

 

def salvar_candidatura(nome, vaga_id, arquivo=ARQUIVO): 

    """Acrescenta uma linha no fim do arquivo, no formato nome;vaga_id. 

 

    Exemplo: salvar_candidatura("Ana Souza", 2) escreve a linha  Ana Souza;2 

    """ 

    # Missão 6 

    
def salvar_candidatura(nome, vaga_id, arquivo=ARQUIVO):
    """Acrescenta uma linha no fim do arquivo, no formato nome;vaga_id."""

    with open(arquivo, "a", encoding="utf-8") as f:
        f.write(f"{nome};{vaga_id}\n")

    # Missão 6
    

 

 

def ler_candidaturas(arquivo=ARQUIVO): 

    """Devolve a lista de candidaturas do arquivo, cada uma como dicionário. 

 

    Exemplo: [{"nome": "Ana Souza", "vaga_id": 2}] 

    O vaga_id volta como número inteiro. 

    Se o arquivo ainda não existir, devolve uma lista vazia. 

    """ 

    # Missão 7 

    
def ler_candidaturas(arquivo=ARQUIVO):
    """Devolve a lista de candidaturas do arquivo."""

    if not os.path.exists(arquivo):
        return []

    candidaturas = []

    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()

            if not linha:
                continue

            nome, vaga_id = linha.split(";")

            candidaturas.append({
                "nome": nome,
                "vaga_id": int(vaga_id)
            })

    return candidaturas


 

 

def ja_se_candidatou(nome, vaga_id, arquivo=ARQUIVO): 

    """Devolve True se essa pessoa já se candidatou a essa vaga, e False se não.""" 

    # Missão 8 

    
def ja_se_candidatou(nome, vaga_id, arquivo=ARQUIVO):
    """Devolve True se essa pessoa já se candidatou a essa vaga, e False se não."""

    candidaturas = ler_candidaturas(arquivo)

    for candidatura in candidaturas:
        if candidatura["nome"] == nome and candidatura["vaga_id"] == vaga_id:
            return True

    return False


 

 

def excluir_candidatura(nome, vaga_id, arquivo=ARQUIVO): 

    """Apaga do arquivo a candidatura dessa pessoa para essa vaga. 

 

    Devolve True se apagou e False se não encontrou a candidatura. 

    As outras linhas continuam no arquivo, na mesma ordem. 

    """ 

    # Missão 9 

    
def excluir_candidatura(nome, vaga_id, arquivo=ARQUIVO):
    """Apaga do arquivo a candidatura dessa pessoa para essa vaga."""

    candidaturas = ler_candidaturas(arquivo)

    restantes = []

    for candidatura in candidaturas:
        if not (candidatura["nome"] == nome and candidatura["vaga_id"] == vaga_id):
            restantes.append(candidatura)

    if len(restantes) == len(candidaturas):
        return False

    with open(arquivo, "w", encoding="utf-8") as f:
        for candidatura in restantes:
            f.write(f'{candidatura["nome"]};{candidatura["vaga_id"]}\n')

    return True
