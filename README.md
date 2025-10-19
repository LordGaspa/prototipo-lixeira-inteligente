# Protótipo Lógico: Lixeira Inteligente (Co-criada com IA)

Este projeto é um protótipo lógico em Python que simula o "cérebro" de uma lixeira inteligente (Smart Bin) baseada em IoT e Robótica. O objetivo é demonstrar como a IA Generativa pode ser usada para a classificação de resíduos em tempo real.

O algoritmo foi desenvolvido para ser a base de um projeto de robótica (como os ministrados nas aulas de Pensamento Computacional), conectando-se a componentes de hardware (câmera, motores) para automatizar a separação de lixo.

**Nota de Desenvolvimento:** Este projeto foi arquitetado e desenvolvido usando Engenharia de Prompts (Gemini) para prototipar a lógica de controle e a simulação de hardware.

---

## 🚀 Funcionalidades Principais

* **Loop de Execução Contínua:** O script roda em um loop (`while True`) simulando um dispositivo de IoT que está sempre "aguardando" um novo item.
* **Simulação de Hardware (Funções Mock):**
    * `capturar_imagem()`: Simula a ativação de uma câmera para capturar a imagem do resíduo.
    * `mover_plataforma()`: Simula a ativação de motores ou servomotores para direcionar o lixo para o compartimento correto.
* **Simulação de IA (Mock):**
    * `analisar_imagem_com_ia()`: Simula a chamada a uma API de IA (como Gemini/Vertex AI), que analisaria a imagem e retornaria uma identificação (ex: "garrafa pet").
* **Lógica de Classificação:** Um algoritmo central que recebe a resposta da IA (string) e a classifica em categorias pré-definidas (Orgânico, Papel/Plástico, Metal/Vidro), antes de acionar o motor correspondente.

---

## 🛠️ Stack de Tecnologia

* **Python** (usando bibliotecas padrão como `time` e `random`)
* **Lógica de Algoritmos & Automação**
* **Conceitos de IoT (Internet of Things) & Robótica**
* **Engenharia de Prompts (Gemini):** Para co-criação da lógica de controle.

---

## ⚙️ Como Executar

1.  Nenhuma instalação é necessária (apenas Python).
2.  Execute o script:
    `python seu_script_lixeira.py` (ou o nome do seu arquivo principal)
3.  O console mostrará o log da lixeira simulando a detecção e classificação de itens a cada 5 segundos.
