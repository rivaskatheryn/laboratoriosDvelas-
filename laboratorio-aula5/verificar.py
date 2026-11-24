"""Verificador do laboratório DevElas. 

 

Rode  python verificar.py  depois de cada missão para ver o seu progresso. 

Você não precisa mudar nada neste arquivo. 

""" 

import os 

import tempfile 

 

try: 

    import candidaturas 

    import ferramentas 

    from vagas_lab import VAGAS 

except SyntaxError as erro: 

    nome = os.path.basename(erro.filename) 

    print(f"\nTem algo digitado errado em {nome}, linha {erro.lineno}.") 

    print("Confira essa linha (e a de cima), salve e rode de novo.\n") 

    raise SystemExit 

 

A_FAZER = "a fazer" 

 

 

def escrever(caminho, texto): 

    with open(caminho, "w", encoding="utf-8") as f: 

        f.write(texto) 

 

 

def ler(caminho): 

    if not os.path.exists(caminho): 

        return None 

    with open(caminho, encoding="utf-8") as f: 

        return f.read() 

 

 

# ---------- Nível 1: funções ---------- 

 

def missao_1(): 

    r = ferramentas.resumo_vaga(VAGAS[0]) 

    if r is None: 

        return A_FAZER + ". A resposta sai com return (o print só mostra na tela)" 

    esperado = "Desenvolvedora Python Júnior - Nuvem Azul Tecnologia (Híbrido)" 

    if r != esperado: 

        return f"esperava {esperado!r}, mas veio {r!r}" 

    if ferramentas.resumo_vaga(VAGAS[4]) != "Designer UX Júnior - Raiz Software (Remoto)": 

        return "funcionou na vaga 1, mas não na vaga 5: use os dados da vaga recebida" 

 

 

def missao_2(): 

    r = ferramentas.buscar_vaga(VAGAS, 3) 

    if r is None: 

        return A_FAZER 

    if not isinstance(r, dict): 

        return "devolva o dicionário inteiro da vaga, não só um pedaço dela" 

    if r is not VAGAS[2]: 

        return f"buscar_vaga(VAGAS, 3) devolveu a vaga de id {r.get('id')}" 

    if ferramentas.buscar_vaga(VAGAS, 99) is not None: 

        return "com um id que não existe, a função deve devolver None" 

 

 

def missao_3(): 

    r = ferramentas.vagas_da_modalidade(VAGAS, "Remoto") 

    if r is None: 

        return A_FAZER 

    if len(VAGAS) != 5: 

        return "a lista original mudou: monte uma lista nova, sem apagar nada de VAGAS" 

    if r != [VAGAS[1], VAGAS[4]]: 

        return f"para Remoto, esperava as vagas 2 e 5, e vieram {len(r)} vaga(s)" 

    if ferramentas.vagas_da_modalidade(VAGAS, "Presencial") != [VAGAS[2], VAGAS[3]]: 

        return "Remoto funcionou, mas Presencial não: use o parâmetro modalidade" 

    if ferramentas.vagas_da_modalidade(VAGAS, "Na Lua") != []: 

        return "se nenhuma vaga for da modalidade, devolva uma lista vazia" 

 

 

def missao_4(): 

    r = ferramentas.contar_por_modalidade(VAGAS) 

    if r is None: 

        return A_FAZER 

    esperado = {"Híbrido": 1, "Remoto": 2, "Presencial": 2} 

    if r != esperado: 

        return f"esperava {esperado}, mas veio {r}" 

    tres = [{"modalidade": "Remoto"}, {"modalidade": "Remoto"}, {"modalidade": "Remoto"}] 

    if ferramentas.contar_por_modalidade(tres) != {"Remoto": 3}: 

        return "com 3 vagas remotas, esperava {'Remoto': 3}: conte a partir da lista recebida" 

    if ferramentas.contar_por_modalidade([]) != {}: 

        return "com uma lista vazia, devolva um dicionário vazio" 

 

 

def missao_5(): 

    r = ferramentas.compatibilidade(VAGAS[1], ["Python", "Excel"]) 

    if r is None: 

        return A_FAZER 

    if not isinstance(r, int): 

        return f"veio {r!r}: devolva um número inteiro (dica: use // ou int())" 

    if r != 66: 

        return f"a vaga 2 pede Python, SQL e Excel; com Python e Excel esperava 66, mas veio {r}" 

    if ferramentas.compatibilidade(VAGAS[1], ["Python", "SQL", "Excel", "Git"]) != 100: 

        return "skills a mais não contam contra: divida pela quantidade de skills da VAGA" 

    if ferramentas.compatibilidade(VAGAS[2], []) != 0: 

        return "sem nenhuma skill, a compatibilidade é 0" 

    try: 

        sem_skills = ferramentas.compatibilidade({"skills": []}, ["Python"]) 

    except ZeroDivisionError: 

        return "e se a vaga não pedir nenhuma skill? Não dá para dividir por zero: devolva 0" 

    if sem_skills != 0: 

        return "se a vaga não pedir nenhuma skill, devolva 0" 

 

 

# ---------- Nível 2: arquivos ---------- 

 

def missao_6(): 

    with tempfile.TemporaryDirectory() as pasta: 

        caminho = os.path.join(pasta, "teste.txt") 

        candidaturas.salvar_candidatura("Lúcia Lima", 3, arquivo=caminho) 

        candidaturas.salvar_candidatura("Ana Souza", 2, arquivo=caminho) 

        try: 

            texto = ler(caminho) 

        except UnicodeDecodeError: 

            return "o acento saiu estranho: use encoding=\"utf-8\" no open" 

        if texto is None: 

            return A_FAZER 

        if texto == "Ana Souza;2\n": 

            return "só a última candidatura ficou: abra o arquivo no modo \"a\" (acrescentar)" 

        if texto == "Lúcia Lima;3Ana Souza;2": 

            return "as candidaturas ficaram grudadas: termine cada linha com \\n" 

        if texto != "Lúcia Lima;3\nAna Souza;2\n": 

            return f"esperava as linhas 'Lúcia Lima;3' e 'Ana Souza;2', e o arquivo ficou {texto!r}" 

 

 

def missao_7(): 

    with tempfile.TemporaryDirectory() as pasta: 

        caminho = os.path.join(pasta, "teste.txt") 

        escrever(caminho, "Ana Souza;2\nLúcia Lima;5\n") 

        try: 

            r = candidaturas.ler_candidaturas(arquivo=caminho) 

        except IndexError: 

            return "cuidado com a linha vazia do fim do arquivo: pule as linhas vazias" 

        if r is None: 

            return A_FAZER 

        esperado = [{"nome": "Ana Souza", "vaga_id": 2}, {"nome": "Lúcia Lima", "vaga_id": 5}] 

        if r != esperado: 

            if r and isinstance(r[0], dict) and r[0].get("vaga_id") == "2": 

                return "o vaga_id veio como texto: transforme em número com int()" 

            if r and isinstance(r[0], dict) and str(r[0].get("vaga_id", "")).endswith("\n"): 

                return "sobrou o \\n do fim da linha: use .strip()" 

            return f"esperava {esperado}, mas veio {r}" 

        try: 

            vazio = candidaturas.ler_candidaturas(arquivo=os.path.join(pasta, "nao_existe.txt")) 

        except FileNotFoundError: 

            return "se o arquivo não existir, devolva uma lista vazia (dica: os.path.exists)" 

        if vazio != []: 

            return "se o arquivo não existir, devolva uma lista vazia" 

 

 

def missao_8(): 

    with tempfile.TemporaryDirectory() as pasta: 

        caminho = os.path.join(pasta, "teste.txt") 

        escrever(caminho, "Ana Souza;2\nLúcia Lima;5\n") 

        r = candidaturas.ja_se_candidatou("Ana Souza", 2, arquivo=caminho) 

        if r is None: 

            return A_FAZER 

        if r is not True: 

            return "Ana Souza se candidatou à vaga 2: esperava True" 

        if candidaturas.ja_se_candidatou("Ana Souza", 5, arquivo=caminho) is not False: 

            return "Ana Souza não se candidatou à vaga 5: esperava False" 

        if candidaturas.ja_se_candidatou("Lúcia Lima", 5, arquivo=caminho) is not True: 

            return "Lúcia Lima se candidatou à vaga 5: esperava True" 

        nao_existe = os.path.join(pasta, "nao_existe.txt") 

        if candidaturas.ja_se_candidatou("Ana Souza", 2, arquivo=nao_existe) is not False: 

            return "sem arquivo, ninguém se candidatou ainda: esperava False" 

 

 

def missao_9(): 

    with tempfile.TemporaryDirectory() as pasta: 

        caminho = os.path.join(pasta, "teste.txt") 

        original = "Ana Souza;2\nLúcia Lima;5\nBia Rocha;1\n" 

        escrever(caminho, original) 

        r = candidaturas.excluir_candidatura("Lúcia Lima", 5, arquivo=caminho) 

        if r is None and ler(caminho) == original: 

            return A_FAZER 

        texto = ler(caminho) 

        if texto != "Ana Souza;2\nBia Rocha;1\n": 

            return f"depois de excluir Lúcia Lima, esperava só Ana e Bia no arquivo, e ficou {texto!r}" 

        if r is not True: 

            return "a candidatura foi apagada: a função deve devolver True" 

        if candidaturas.excluir_candidatura("Lúcia Lima", 5, arquivo=caminho) is not False: 

            return "excluir algo que não existe deve devolver False" 

        if ler(caminho) != "Ana Souza;2\nBia Rocha;1\n": 

            return "excluir algo que não existe não pode mudar o arquivo" 

 

 

MISSOES = [ 

    (1, "Resumo da vaga", missao_1), 

    (2, "Buscar vaga pelo id", missao_2), 

    (3, "Filtro por modalidade", missao_3), 

    (4, "Contagem por modalidade", missao_4), 

    (5, "Compatibilidade", missao_5), 

    (6, "Salvar candidatura", missao_6), 

    (7, "Ler candidaturas", missao_7), 

    (8, "Candidatura repetida", missao_8), 

    (9, "Excluir candidatura", missao_9), 

] 

 

 

def main(): 

    print("\n=== Laboratório DevElas: verificador ===\n") 

    prontas = 0 

    proxima = None 

    for numero, titulo, teste in MISSOES: 

        try: 

            resultado = teste() 

        except Exception as erro: 

            resultado = f"o código deu erro: {type(erro).__name__}: {erro}" 

        if resultado is None: 

            prontas += 1 

            print(f"✅ Missão {numero} · {titulo}") 

            continue 

        if proxima is None: 

            proxima = numero 

        if resultado.startswith(A_FAZER): 

            print(f"⏳ Missão {numero} · {titulo}") 

            extra = resultado[len(A_FAZER):].lstrip(". ") 

            if extra: 

                print(f"   Pista: {extra}") 

        else: 

            print(f"❌ Missão {numero} · {titulo}") 

            print(f"   Pista: {resultado}") 

    barra = "■" * prontas + "□" * (len(MISSOES) - prontas) 

    print(f"\nProgresso: {prontas} de {len(MISSOES)}  {barra}") 

    if proxima is None: 

        print("Todas as missões com verificador estão prontas! Siga para a missão 10.\n") 

    else: 

        print(f"Próxima parada: missão {proxima}.\n") 

 

 

main() 