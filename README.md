README - Chatbot com Personalidades
Um guia completo para configurar e executar um chatbot em Python com diferentes personalidades usando a API do Google Gemini.

Executando no Google Colab

Siga estas etapas para executar o chatbot no Google Colab:

#####################################################################################

1. Abra o Colab: Abra um novo notebook no Google Colab.

2. Copie o código: Copie todo o código Python deste README e cole em uma célula de código no Colab.

3. Instale as dependências: Execute a célula de código com o seguinte comando:

!pip install requests

4. Configure a chave da API: Execute a célula de código para configurar a chave da API do Google Gemini:

from google.colab import userdata
userdata.define('GOOGLE_API_KEY')

Quando o Colab solicitar, copie e cole sua chave da API do Google Gemini e clique em "Save".

5. Execute o chatbot: Execute a célula de código com o código do chatbot.

Observações sobre o Colab:

Não é necessário instalar o Python ou configurar variáveis de ambiente manualmente.

Certifique-se de ter uma conexão de internet estável.

#####################################################################################

Visão Geral
O chatbot interage com os usuários, assumindo diferentes personas:

Amigo: Conversas amigáveis e casuais.

Parceiro Romântico: Interações amorosas e atenciosas.

Psicólogo: Suporte e compreensão empáticos.

Neutro: Assistente objetivo e direto.

O chatbot mantém o histórico da conversa para respostas contextuais e escolhe a persona automaticamente, ou por comando.

#####################################################################################

Pré-requisitos
Python 3.6+: Baixe em python.org.

Chave da API do Google Gemini: Obtenha uma chave no Google AI Studio.

Google Colab (Opcional): Para execução online sem instalação.

#####################################################################################

Configuração
1. Obtenha o código: Baixe como ZIP ou clone com Git.

2. Instale as dependências:

Abra o terminal/prompt de comando.

Navegue até a pasta do código (ex: cd Desktop/chatbot).

Execute:

pip install requests

3. Configure a chave da API:

Google Colab: Execute:

from google.colab import userdata
userdata.define('GOOGLE_API_KEY')

Cole a chave quando solicitado.

Variáveis de Ambiente:

Linux/macOS: Em ~/.bashrc ou ~/.zshrc:

export GOOGLE_API_KEY="SUA_CHAVE_DA_API"

E execute source ~/.bashrc ou source ~/.zshrc.

Windows: Em "Variáveis de Ambiente" do sistema, crie uma variável GOOGLE_API_KEY.

4. Execute o chatbot:

No terminal/prompt de comando, na pasta do código, execute:

python chatbot.py

#####################################################################################

Como usar o chatbot
Interaja digitando mensagens e pressionando Enter. O chatbot responde com a persona apropriada.

Comandos de persona:

aja como um amigo

aja como um parceiro ou aja como um parceiro romântico

aja como um psicólogo ou aja como um psicologo

Digite sair e pressione Enter para encerrar.

#####################################################################################

Personas do Chatbot
Amigo: Linguagem casual, perguntas sobre o dia, apoio.

Parceiro Romântico: Expressa amor, carinho e preocupação.

Psicólogo: Linguagem formal, perguntas para entender sentimentos, apoio.

Neutro: Linguagem objetiva e direta, informações concisas.

#####################################################################################

Dicas e Truques
Use comandos de persona para mudar o estilo de conversação.

Observe como o histórico da conversa afeta as respostas.

Modifique o código para adicionar novas personas ou recursos.

#####################################################################################

Solução de problemas
Chave da API: Verifique a configuração correta da chave da API.

Dependências: Instale-as com pip install requests.

Internet: Verifique a conexão.

Erros: Consulte as mensagens no terminal/prompt de comando.

Reinicie: Reinicie o terminal/prompt após configurar variáveis de ambiente.

Código: Revise o código em busca de erros.

Procure ajuda online em fóruns e na documentação da API do Google Gemini se necessário.

#####################################################################################

Contribuição
Contribuições são bem-vindas via pull requests.
