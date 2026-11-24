"""Ferramentas do laboratório DevElas. 

 

Cada função recebe dados, faz um trabalho e devolve a resposta com return. 

""" 

 

 

def resumo_vaga(vaga): 

    """Devolve uma linha de texto com o resumo da vaga. 

 

    Formato: título - empresa (modalidade) 

    Exemplo: "Desenvolvedora Python Júnior - Nuvem Azul Tecnologia (Híbrido)" 

    """ 

    # Missão 1: troque o pass pelo seu código 

    return f"{vaga['titulo']} - {vaga['empresa']} ({vaga['modalidade']})"

 

 

def buscar_vaga(vagas, vaga_id): 

    """Devolve a vaga (o dicionário inteiro) que tem esse id. 

 

    Se nenhuma vaga tiver esse id, devolve None. 

    Exemplo: buscar_vaga(VAGAS, 3) devolve a vaga da Pixel Lab. 

    """ 

    # Missão 2 

    
def buscar_vaga(vagas, vaga_id):
    """Devolve a vaga (o dicionário inteiro) que tem esse id.

    Se nenhuma vaga tiver esse id, devolve None.
    """
    for vaga in vagas:
        if vaga["id"] == vaga_id:
            return vaga

    return None


 

 

def vagas_da_modalidade(vagas, modalidade): 

    """Devolve uma lista nova só com as vagas da modalidade pedida. 

 

    Exemplo: vagas_da_modalidade(VAGAS, "Remoto") devolve as 2 vagas remotas. 

    """ 

    # Missão 3 

    
def vagas_da_modalidade(vagas, modalidade):
    """Devolve uma lista nova só com as vagas da modalidade pedida."""

    resultado = []

    for vaga in vagas:
        if vaga["modalidade"] == modalidade:
            resultado.append(vaga)

    return resultado


 

 

def contar_por_modalidade(vagas): 

    """Devolve um dicionário com quantas vagas existem em cada modalidade. 

 

    Exemplo: {"Híbrido": 1, "Remoto": 2, "Presencial": 2} 

    """ 

    # Missão 4 

    def contar_por_modalidade(vagas):
        """Devolve um dicionário com quantas vagas existem em cada modalidade."""

    contagem = {}

    for vaga in vagas:
        modalidade = vaga["modalidade"]
        contagem[modalidade] = contagem.get(modalidade, 0) + 1

    return contagem

 

 

def compatibilidade(vaga, minhas_skills): 

    """Devolve, de 0 a 100, quanto as suas skills combinam com as da vaga. 

 

    Conta quantas skills da vaga aparecem em minhas_skills e devolve a 

    porcentagem como número inteiro, arredondada para baixo. 

    Exemplo: a vaga pede Python, SQL e Excel e você tem Python e Excel: 

    2 de 3, então a função devolve 66. 

    Se a vaga não pedir nenhuma skill, devolve 0. 

    """ 

    # Missão 5 

    
def compatibilidade(vaga, minhas_skills):
    """Devolve, de 0 a 100, quanto as suas skills combinam com as da vaga."""

    skills_vaga = vaga["skills"]

    if len(skills_vaga) == 0:
        return 0

    acertos = 0

    for skill in skills_vaga:
        if skill in minhas_skills:
            acertos += 1

    return acertos * 100 // len(skills_vaga)
