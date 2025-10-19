# Importando bibliotecas que seriam úteis no futuro
# A biblioteca 'time' nos permite fazer pausas no programa
import time

# --- ETAPA DE SIMULAÇÃO (Imagine que estas funções conversam com as peças reais) ---


def capturar_imagem():
    """
    Função de mentirinha que simula a câmera tirando uma foto.
    Em um projeto real, aqui estaria o código para controlar a câmera.
    """
    print("📸 Câmera ativada... Capturando imagem do objeto.")
    # Vamos retornar o nome de um arquivo de imagem de exemplo
    return "imagem_do_lixo.jpg"


def analisar_imagem_com_ia(caminho_da_imagem):
    """
    Função de mentirinha que simula a análise pela IA (Gemini).
    Ela recebe o nome da imagem e "adivinha" o que é.
    """
    print(f"🧠 Enviando '{caminho_da_imagem}' para análise da IA...")
    time.sleep(2)  # Simula o tempo de análise

    # Para nosso teste, vamos retornar um tipo de lixo aleatório.
    # Em um projeto real, aqui você faria a chamada para a API do Gemini.
    # Exemplo de possíveis respostas da IA:
    tipos_de_lixo = [
        "casca de banana",
        "garrafa pet",
        "lata de refrigerante",
        "folha de papel",
        "caco de vidro",
    ]
    import random

    return random.choice(tipos_de_lixo)


def mover_plataforma(posicao):
    """
    Função de mentirinha que simula o movimento do motor.
    """
    print(f"💪 Movendo plataformas para a posição: '{posicao}'...")
    time.sleep(1)  # Simula o tempo de movimento
    print(f"✅ Lixo destinado para '{posicao}'. Plataformas na posição inicial.")


# --- O ALGORITMO PRINCIPAL (O Cérebro do Projeto) ---

print("--- Lixeira Inteligente v1.0 - Iniciando ---")

# Este loop 'while True' faz o programa rodar para sempre, esperando por lixo.
while True:
    # 1. Espera - Vamos simular a detecção de um lixo novo a cada 5 segundos
    print("\n-------------------------------------------------")
    print("Aguardando novo item... (Pressione Ctrl+C para sair)")
    time.sleep(5)

    # 2. Captura a Imagem
    imagem_capturada = capturar_imagem()

    # 3. Analisa com a IA
    resultado_ia = analisar_imagem_com_ia(imagem_capturada)
    print(f"🔍 A IA identificou o objeto como: '{resultado_ia}'")

    # 4. Classifica o Resultado
    if "casca" in resultado_ia or "resto de comida" in resultado_ia:
        categoria = "Orgânico"
    elif "papel" in resultado_ia or "pet" in resultado_ia or "plástico" in resultado_ia:
        categoria = "Papel e Plástico"
    elif "lata" in resultado_ia or "metal" in resultado_ia or "vidro" in resultado_ia:
        categoria = "Metal e Vidro"
    else:
        categoria = "Não Identificado"  # Uma categoria para erros

    print(f"🏷️ Classificado na categoria: '{categoria}'")

    # 5. Age (Move as Plataformas)
    if categoria != "Não Identificado":
        mover_plataforma(categoria)
    else:
        print("❌ Não foi possível identificar o lixo. Descarte manual necessário.")
