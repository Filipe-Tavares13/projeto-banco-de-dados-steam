# ==============================================================================    
# PROJETO DE BANCO DE DADOS I - FASE 01 (DESCOBERTA E REQUISITOS)
# AVISO DE USO DE IA: Código estruturado com auxílio do Google Gemini.
# Link público da conversa: [https://share.gemini.google/cyr9j14l0zl2]
# ==============================================================================

import requests
import json

# 1. OBTENÇÃO DOS DADOS VIA API (SteamSpy - Top 100 jogos nas últimas 2 semanas)
url = "https://steamspy.com/api.php?request=top100in2weeks"
print("Baixando dados da API da SteamSpy...")
resposta = requests.get(url)

if resposta.status_code == 200:
    dados_brutos = resposta.json()
    
    # Salvando a cópia dos dados originais (exigência do entregável)
    with open("dados_originais_steam.json", "w", encoding="utf-8") as f:
        json.dump(dados_brutos, f, indent=4, ensure_ascii=False)
    print("-> 'dados_originais_steam.json' salvo com sucesso!\n")

    # 2. ANÁLISE PRELIMINAR E TRATAMENTO DE PROBLEMAS
    dados_organizados = []
    problemas = {"preco_invalido_ou_zero": 0, "sem_publisher": 0, "tempo_jogo_zero": 0}

    # A API retorna um dicionário onde a chave é o ID do jogo
    for appid, info in dados_brutos.items():
        # Identificando problemas nos dados brutos:
        # Problema 1: Preço vem em centavos e como texto (string), ou zerado
        preco_raw = int(info.get("price") or 0)
        if preco_raw == 0:
            problemas["preco_invalido_ou_zero"] += 1
            
        # Problema 2: Jogos sem publicadora (publisher) cadastrada
        publisher = info.get("publisher", "").strip()
        if not publisher:
            problemas["sem_publisher"] += 1
            publisher = "Desconhecida"
            
        # Problema 3: Tempo médio jogado igual a zero (erro de coleta da Steam)
        tempo_medio = info.get("average_forever", 0)
        if tempo_medio == 0:
            problemas["tempo_jogo_zero"] += 1

        # Montando o registro limpo e padronizado
        jogo_limpo = {
            "appid": info.get("appid"),
            "nome": info.get("name"),
            "desenvolvedora": info.get("developer", "Desconhecida").strip(),
            "publicadora": publisher,
            "positivas": info.get("positive", 0),
            "negativas": info.get("negative", 0),
            "tempo_medio_horas": round(tempo_medio / 60, 2), # Convertendo minutos para horas
            "preco_dolares": round(preco_raw / 100, 2),      # Convertendo centavos para dólares
            "faixa_donos": info.get("owners")
        }
        dados_organizados.append(jogo_limpo)

    # 3. SALVANDO OS DADOS ORGANIZADOS
    with open("dados_organizados_steam.json", "w", encoding="utf-8") as f:
        json.dump(dados_organizados, f, indent=4, ensure_ascii=False)

    # Exibindo o resumo da análise no terminal para ajudar nos slides
    print("=== RELATÓRIO DA ANÁLISE PRELIMINAR ===")
    print(f"Total de jogos analisados: {len(dados_organizados)}")
    print(f"- Jogos gratuitos ou com falha de preço (0): {problemas['preco_invalido_ou_zero']}")
    print(f"- Jogos com publicadora em branco: {problemas['sem_publisher']}")
    print(f"- Jogos com tempo médio zerado: {problemas['tempo_jogo_zero']}")
    print("-> 'dados_organizados_steam.json' salvo com sucesso!")
else:
    print(f"Erro ao acessar a API: Status {resposta.status_code}")