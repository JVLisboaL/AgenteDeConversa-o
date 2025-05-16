README - Chatbot com Personalidades
Este README fornece um guia completo para configurar e executar um chatbot em Python que utiliza a API do Google Gemini para simular diferentes personalidades. O objetivo é explicar de forma clara e concisa como usar o chatbot, mesmo para pessoas com pouca experiência em programação.

Executando no Google Colab

Se você estiver usando o Google Colab, siga estas etapas para executar o chatbot:

Abra o Colab: Abra um novo notebook no Google Colab.

Copie o código: Copie todo o código Python deste README e cole em uma célula de código no Colab.

Instale as dependências: Execute a célula de código com o seguinte comando para instalar as dependências necessárias:

!pip install requests

Configure a chave da API: Execute a célula de código com o seguinte código para configurar a chave da API do Google Gemini:

from google.colab import userdata
userdata.define('GOOGLE_API_KEY')

Quando o Colab solicitar, copie e cole sua chave da API do Google Gemini e clique em "Save".

Execute o chatbot: Execute a célula de código com o código do chatbot. O chatbot será iniciado e exibirá uma saudação inicial.

Observações sobre o Colab:

Você não precisa instalar o Python ou configurar variáveis de ambiente manualmente no Colab.

Certifique-se de ter uma conexão com a Internet estável.

Visão Geral
O chatbot é projetado para interagir com os usuários, assumindo uma das seguintes personas:

Amigo: Um companheiro amigável e casual, pronto para uma conversa descontraída.

Parceiro Romântico: Um parceiro amoroso e atencioso, ideal para quem busca afeto e romance.

Psicólogo: Um ouvinte empático e compreensivo, que oferece suporte e compreensão.

Neutro: Um assistente objetivo e direto, focado em fornecer informações precisas.

O chatbot mantém um histórico da conversa para fornecer respostas mais contextuais e relevantes. A escolha da persona é feita automaticamente com base nas mensagens do usuário, mas também pode ser controlada por comandos explícitos.

Pré-requisitos
Antes de começar, certifique-se de que você tem o seguinte:

Python 3.6 ou superior: Se você ainda não tem o Python instalado, baixe-o do site oficial (https://www.python.org/downloads/) e siga as instruções de instalação para o seu sistema operacional.

Chave da API do Google Gemini: O chatbot utiliza a API do Google Gemini para gerar respostas. Para obter uma chave de API, siga estas etapas:

Acesse o Google AI Studio.

Crie uma conta ou faça login com sua conta do Google.

No Google AI Studio, crie um novo projeto e, em seguida, crie uma chave de API para o seu projeto.

Google Colab (Opcional): Se você estiver usando o Google Colab, um ambiente de notebook online, você não precisa instalar o Python ou configurar variáveis de ambiente manualmente. O Colab fornece um ambiente pronto para usar, com todas as dependências necessárias pré-instaladas.

Configuração
Siga estas etapas para configurar o chatbot em seu sistema:

Obtenha o código:

Você pode baixar o código diretamente como um arquivo ZIP ou clonar o repositório (se disponível) usando o Git. Se você não estiver familiarizado com o Git, basta baixar o ZIP e extraí-lo em uma pasta em seu computador.

Instale as dependências:

Abra um terminal (no Linux/macOS) ou prompt de comando (no Windows). Se você não sabe como fazer isso, siga estas instruções:

Windows: Pressione a tecla Windows, digite "cmd" e pressione Enter.

Linux/macOS: Pressione Ctrl + Alt + T (Linux) ou Command + Espaço, digite "terminal" e pressione Enter (macOS).

Navegue até o diretório onde você salvou o código do chatbot usando o comando cd. Por exemplo, se você salvou o código na pasta "chatbot" em sua área de trabalho, digite:

cd Desktop/chatbot

Execute o seguinte comando para instalar as bibliotecas necessárias:

pip install requests

Este comando utiliza o pip, o gerenciador de pacotes do Python, para baixar e instalar a biblioteca requests, que é utilizada para fazer requisições à API do Google Gemini.

Configure a chave da API:

A chave da API do Google Gemini precisa ser configurada como uma variável de ambiente para que o chatbot possa acessá-la. Existem duas maneiras de fazer isso:

Usando o Google Colab:

Se você estiver usando o Google Colab, execute a primeira célula de código no notebook, que contém as seguintes linhas:

from google.colab import userdata

userdata.define('GOOGLE_API_KEY')

Isso definirá um "segredo" no Colab, onde você pode armazenar sua chave de API com segurança. Quando o Colab solicitar o valor, copie e cole sua chave da API do Google Gemini e clique em "Save".

Usando variáveis de ambiente:

Se você não estiver usando o Google Colab, você precisa definir a variável de ambiente GOOGLE_API_KEY no seu sistema operacional.

No Linux/macOS:

Abra o arquivo de configuração do seu shell (geralmente ~/.bashrc ou ~/.zshrc) em um editor de texto. Você pode usar o nano, por exemplo:

nano ~/.bashrc

Adicione a seguinte linha ao final do arquivo:

export GOOGLE_API_KEY="SUA_CHAVE_DA_API"

Substitua "SUA_CHAVE_DA_API" pela sua chave de API real.

Salve o arquivo e feche o editor.

Execute o seguinte comando para atualizar o ambiente:

source ~/.bashrc

No Windows:

Abra o Painel de Controle.

Vá para "Sistema e Segurança" -> "Sistema" -> "Configurações avançadas do sistema".

Na guia "Avançado", clique em "Variáveis de Ambiente".

Em "Variáveis do sistema", clique em "Novo...".

Na janela "Nova Variável do Sistema", defina o nome da variável como GOOGLE_API_KEY e o valor como sua chave da API do Google Gemini.

Clique em "OK" em todas as janelas para salvar as alterações.

Execute o chatbot:

Abra um terminal ou prompt de comando.

Navegue até o diretório onde você salvou o código do chatbot usando o comando cd (conforme explicado na etapa 2).

Execute o seguinte comando para iniciar o chatbot:

python chatbot.py

O chatbot será iniciado e exibirá uma saudação inicial.

Como usar o chatbot
Depois de executar o chatbot, você pode interagir com ele digitando suas mensagens e pressionando a tecla Enter. O chatbot responderá de acordo com a persona atual, que é selecionada automaticamente com base no contexto da conversa.

Você também pode usar comandos explícitos para mudar a persona do chatbot:

aja como um amigo

aja como um parceiro ou aja como um parceiro romântico

aja como um psicólogo ou aja como um psicologo

Para encerrar a conversa, digite sair e pressione Enter.

Personas do Chatbot em Detalhe
Aqui estão mais detalhes sobre o comportamento de cada persona:

Amigo:

Utiliza uma linguagem casual e amigável, com gírias e expressões informais.

Demonstra interesse genuíno em seus assuntos, fazendo perguntas sobre o seu dia e oferecendo apoio.

Cria uma atmosfera descontraída e divertida, como se estivesse conversando com um amigo próximo.

Parceiro Romântico:

Expressa amor, carinho e afeto de forma sincera e apaixonada.

Utiliza uma linguagem romântica e envolvente, com declarações de amor, elogios e demonstrações de saudade.

Transmite cuidado e preocupação com o seu bem-estar, oferecendo conforto e apoio emocional.

Psicólogo:

Utiliza uma linguagem formal e empática, demonstrando compreensão e respeito por seus sentimentos.

Faz perguntas abertas e reflexivas para te ajudar a explorar seus pensamentos e emoções.

Oferece apoio e compreensão, sem fazer julgamentos ou dar conselhos precipitados.

Neutro:

Utiliza uma linguagem objetiva e direta, focada em fornecer informações precisas e relevantes.

Responde às suas perguntas de forma concisa e clara, sem expressar emoções ou opiniões pessoais.

Comporta-se como um assistente virtual eficiente e informativo.

Dicas e Truques
Experimente usar os comandos de persona para explorar os diferentes estilos de conversação do chatbot. Observe como a linguagem, o tom e o comportamento mudam de acordo com a persona selecionada.

Preste atenção em como o chatbot utiliza o histórico da conversa para manter o contexto e fornecer respostas mais coerentes. Isso demonstra a capacidade do modelo de entender e acompanhar o fluxo da conversa.

Sinta-se à vontade para modificar o código do chatbot para adicionar novas personas, personalizar as respostas existentes ou aprimorar a lógica de seleção de persona. Este é um projeto de código aberto, e suas contribuições são bem-vindas!

Solução de problemas
Se você encontrar algum problema ao configurar ou usar o chatbot, aqui estão algumas dicas para solucionar os problemas mais comuns:

Chave da API: Verifique se você configurou corretamente a chave da API do Google Gemini, seguindo as instruções na seção "Configuração" deste README. Certifique-se de que a chave está correta e de que você a definiu como uma variável de ambiente ou segredo do Colab.

Dependências: Certifique-se de que você instalou todas as dependências necessárias usando o comando pip install requests. Se você esqueceu de instalar as dependências, o chatbot pode apresentar erros ao tentar importar a biblioteca requests.

Conexão com a Internet: O chatbot precisa de uma conexão ativa com a Internet para se comunicar com a API do Google Gemini. Verifique se você está conectado à Internet e se sua conexão está funcionando corretamente.

Erros no terminal/prompt de comando: Preste atenção a quaisquer mensagens de erro que possam aparecer no terminal ou prompt de comando. Essas mensagens podem fornecer pistas valiosas sobre a causa do problema. Se você não conseguir entender o erro, copie a mensagem e pesquise online por uma solução.

Reinicie o terminal/prompt de comando: Após definir a variável de ambiente GOOGLE_API_KEY, pode ser necessário reiniciar o terminal ou prompt de comando para que a alteração tenha efeito.

Verifique o código: Se você modificou o código do chatbot, revise suas alterações com cuidado para garantir que não há erros de sintaxe ou lógica. Use um editor de código com destaque de sintaxe e verificação de erros para facilitar a identificação de problemas.

Se você ainda estiver com problemas, não hesite em procurar ajuda online em fóruns de programação, comunidades de desenvolvedores ou na documentação da API do Google Gemini.

Contribuição
Contribuições para este projeto são bem-vindas! Se você tiver alguma ideia para melhorar o chatbot, como adicionar novas personas, aprimorar as respostas ou corrigir bugs, sinta-se à vontade para enviar um pull request no repositório do projeto.
