# Chatbot com Personalidades

Um guia completo para configurar e executar um chatbot em Python com diferentes personalidades usando a API do Google Gemini.

## Visão Geral

Este chatbot foi projetado para interagir com os usuários, assumindo uma de quatro personas distintas:

- *Amigo*: Um companheiro amigável e casual, pronto para uma conversa descontraída.
- *Parceiro Romântico*: Um parceiro amoroso e atencioso, ideal para quem busca afeto e romance.
- *Psicólogo*: Um ouvinte empático e compreensivo, que oferece suporte e compreensão.
- *Neutro*: Um assistente objetivo e direto, focado em fornecer informações precisas e factuais.

O chatbot mantém um histórico da conversa para fornecer respostas mais contextuais e relevantes. A escolha da persona é feita automaticamente com base nas mensagens do usuário, mas também pode ser controlada por comandos explícitos.

## Funcionalidades

- Interação em linguagem natural com o usuário
- Seleção automática de persona com base no contexto da conversa
- Comandos explícitos para mudar a persona do chatbot
- Histórico da conversa para respostas contextuais
- Fácil configuração e execução

## Como usar

### Executando no Google Colab

Se você estiver usando o Google Colab, siga estas etapas para executar o chatbot:

1. *Abra o Colab*: Abra um novo notebook no Google Colab.
2. *Copie o código*: Copie todo o código Python deste README e cole em uma célula de código no Colab.
3. *Instale as dependências*: Execute a célula de código com o seguinte comando:

```
!pip install requests
```

*Configure a chave da API*: Execute a célula de código para configurar a chave da API do Google Gemini:


from google.colab import userdata
userdata.define('GOOGLE_API_KEY')


Quando o Colab solicitar, copie e cole sua chave da API do Google Gemini e clique em *"Save"*.

### Execute o chatbot

Execute a célula de código com o código do chatbot.

## Configuração

Se você estiver executando o chatbot localmente, siga estas etapas:

1. *Instale o Python*:  
   Certifique-se de ter o Python 3.6 ou superior instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/).

2. *Instale as dependências*:  
   Abra um terminal ou prompt de comando e execute o seguinte comando:

```
bash

pip install requests
```

3. *Configure a chave da API do Google Gemini*:

- Obtenha uma chave de API do Google Gemini no Google AI Studio.

- Defina a chave da API como uma variável de ambiente chamada ```GOOGLE_API_KEY. ``` 
  Por exemplo, no Linux/macOS, você pode adicionar a seguinte linha ao seu arquivo ```~/.bashrc``` ou ```~/.zshrc:```

bash

export GOOGLE_API_KEY="SUA_CHAVE_DA_API"


Lembre-se de substituir ```"SUA_CHAVE_DA_API"``` pela sua chave de API real.

4. *Execute o chatbot*:

Abra um terminal ou prompt de comando, navegue até o diretório onde você salvou o código do chatbot e execute o seguinte comando:

```
bash

python chatbot.py
```

## Interagindo com o Chatbot

Depois de executar o chatbot, você pode interagir com ele digitando suas mensagens e pressionando Enter. O chatbot responderá de acordo com a persona atual.

Você também pode usar comandos explícitos para mudar a persona do chatbot:

- ```aja como um amigo```
- ```aja como um parceiro``` ou ```aja como um parceiro romântico```
- ```aja como um psicólogo``` ou ```aja como um psicologo```
- ```aja como neutro```

Para encerrar a conversa, digite ```"sair"``` e pressione Enter.

## Solução de Problemas

- *Erro de API Key*: Se você estiver recebendo um erro relacionado à chave da API, verifique se você configurou a variável de ambiente ```GOOGLE_API_KEY``` corretamente.
- *Erro de instalação*: Se você estiver tendo problemas para instalar as dependências, verifique se você tem o Python e o pip instalados corretamente.
- *Chatbot não responde*: Se o chatbot não estiver respondendo, verifique sua conexão com a internet e tente reiniciar o chatbot.

## Contribuição

Contribuições para este projeto são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novos recursos.
