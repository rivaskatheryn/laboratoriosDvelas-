"""Gera o painel.html: uma página com Bootstrap montada a partir dos dados. 

 

Rode com:  python gerar_painel.py  e depois abra o painel.html no navegador. 

""" 

import os 

 

from candidaturas import PASTA, ler_candidaturas 

from ferramentas import compatibilidade, contar_por_modalidade 

from vagas_lab import VAGAS 

 

MINHAS_SKILLS = ["Python", "Git", "HTML"]  # as mesmas do caderno 

 

TOPO = """<!DOCTYPE html> 

<html lang="pt-br"> 

<head> 

  <meta charset="utf-8"> 

  <meta name="viewport" content="width=device-width, initial-scale=1"> 

  <title>Painel do laboratório | DevElas</title> 

  <link rel="stylesheet" 

    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.9/dist/css/bootstrap.min.css"> 

</head> 

<body class="bg-light"> 

  <main class="container py-5"> 

    <h1 class="fw-bold mb-4">Painel do laboratório</h1> 

""" 

 

RODAPE = """  </main> 

</body> 

</html> 

""" 

 

 



def card_da_vaga(vaga, nomes):
    """Cria um card moderno para cada vaga."""

    titulo = vaga["titulo"]
    empresa = vaga["empresa"]
    modalidade = vaga["modalidade"]

    lista_nomes = ""

    if nomes:
        for nome in nomes:
            lista_nomes += f"""
                <li class="list-group-item border-0 px-0 py-2">
                    <span style="color: #6C3483;">●</span>
                    {nome}
                </li>
            """
    else:
        lista_nomes = """
            <li class="list-group-item border-0 px-0 text-muted">
                Ainda não há candidaturas.
            </li>
        """

    return f"""
    <div class="col">
        <div class="card h-100 border-0 shadow-sm rounded-4">

            <div class="card-body p-4">

                <div class="mb-3">
                    <span class="badge rounded-pill"
                          style="background-color: #EDE2F5; color: #6C3483;">
                        {modalidade}
                    </span>
                </div>

                <h5 class="fw-bold mb-2"
                    style="color: #43205F;">
                    {titulo}
                </h5>

                <p class="text-muted mb-3">
                    🏢 {empresa}
                </p>

                <hr style="border-color: #EDE2F5;">

                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="fw-semibold" style="color: #43205F;">
                        Candidaturas
                    </span>

                    <span class="badge rounded-pill"
                          style="background-color: #6C3483;">
                        {len(nomes)}
                    </span>
                </div>

                <ul class="list-group list-group-flush">
                    {lista_nomes}
                </ul>

            </div>
        </div>
    </div>
    """


def tabela_resumo():
    """Cria uma tabela com a quantidade de vagas por modalidade."""

    contagem = contar_por_modalidade(VAGAS)

    linhas = ""

    for modalidade, quantidade in contagem.items():
        linhas += f"""
            <tr>
                <td>{modalidade}</td>
                <td class="text-center fw-bold">{quantidade}</td>
            </tr>
        """

    return f"""
    <div class="card border-0 shadow-sm rounded-4 mb-4">
        <div class="card-body p-4">

            <h4 class="fw-bold mb-3" style="color: #43205F;">
                Resumo das oportunidades
            </h4>

            <div class="table-responsive">
                <table class="table align-middle">
                    <thead>
                        <tr style="color: #6C3483;">
                            <th>Modalidade</th>
                            <th class="text-center">Quantidade</th>
                        </tr>
                    </thead>

                    <tbody>
                        {linhas}
                    </tbody>
                </table>
            </div>

        </div>
    </div>
    """



 

 

def gerar_painel(): 

    candidaturas = ler_candidaturas() 

    html = TOPO

# Missão 13: a tabela-resumo entra aqui
    html += tabela_resumo()

    html += '    <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">\n'
    for vaga in VAGAS: 

        nomes = [] 

        for candidatura in candidaturas: 

            if candidatura["vaga_id"] == vaga["id"]: 

                nomes.append(candidatura["nome"]) 

        html += card_da_vaga(vaga, nomes) 

    html += "    </div>\n" 

    html += RODAPE 

 

    with open(os.path.join(PASTA, "painel.html"), "w", encoding="utf-8") as arquivo: 

        arquivo.write(html) 

    print("painel.html criado! Abra o arquivo no navegador.") 

 

 

gerar_painel() 