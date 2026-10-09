# 👤 Sistema de Autenticação Facial

Este projeto é uma aplicação web simples e completa (Full-Stack) de reconhecimento facial. O sistema simula uma verificação de identidade (como a utilizada em aplicativos de delivery e bancos), comparando a foto de um documento oficial com uma "selfie" em tempo real para determinar se pertencem à mesma pessoa.

## 🚀 Tecnologias Utilizadas

**Front-end:**
* **HTML5 & CSS3:** Estrutura e estilização da interface de upload de fotos.
* **JavaScript (Vanilla):** Lógica para capturar as imagens inseridas pelo usuário e enviá-las de forma assíncrona (`fetch API`) para o nosso servidor.

**Back-end:**
* **Python 3:** Linguagem principal do servidor.
* **Flask:** Micro-framework web utilizado para criar a API que recebe as requisições do front-end.
* **Flask-CORS:** Biblioteca para permitir que o nosso arquivo HTML local comunique com o servidor Flask sem bloqueios de segurança (Cross-Origin Resource Sharing).
* **Face Recognition & Dlib:** As bibliotecas centrais de Inteligência Artificial que fazem o mapeamento e a comparação dos vetores faciais (embeddings) com alta precisão.

## 🧠 Como Funciona?

1. O usuário seleciona duas imagens na interface web (HTML).
2. O JavaScript empacota essas imagens via `FormData` e faz uma requisição `POST` para a rota `/compare` do nosso servidor Flask.
3. O Python recebe as imagens, localiza os rostos e extrai a assinatura matemática de cada um utilizando a biblioteca `face_recognition`.
4. O sistema calcula a distância Euclidiana entre os dois rostos. Se a similaridade for suficiente, ele retorna `match: true` (Acesso Liberado).

## 🚧 Desafios e Aprendizados (Troubleshooting)

Durante o desenvolvimento no ambiente Windows, enfrentamos e superamos alguns obstáculos clássicos de configuração de ambiente para Inteligência Artificial:

1. **Compilação do Dlib (Erro de C++ / CMake):**
   A biblioteca de reconhecimento facial depende do `dlib`, que é escrito em C++. No Windows, o comando `pip install face_recognition` falhou inicialmente (`Failed building wheel for dlib`).
   * **Solução:** Foi necessário instalar o **CMake** via terminal e baixar o pacote de **Visual Studio C++ Build Tools** da Microsoft para que o Python conseguisse compilar a biblioteca nativamente.

2. **Download dos Modelos Matemáticos:**
   Mesmo após a instalação, ao rodar o servidor, o sistema pediu o pacote `face_recognition_models`.
   * **Solução:** Instalamos o pacote diretamente do repositório fonte utilizando o Git pelo comando: `pip install git+https://github.com/ageitgey/face_recognition_models`.

3. **Arquitetura de API vs. Interface Visual (Erro "Not Found"):**
   Ao acessar `127.0.0.1:5000` diretamente no navegador, recebemos um erro "Not Found".
   * **Aprendizado:** Entendemos a separação entre Back-end e Front-end. O servidor Flask foi construído apenas para processar dados (API na rota `/compare`), não para renderizar telas. A interface correta a ser acessada era o próprio arquivo `index.html` rodando localmente no navegador.

## 🛠️ Como executar este projeto na sua máquina

1. Clone este repositório:
   ```bash
   git clone https://github.com/alissonlabs/reconhecimentofacial.git
   ```

2. Instale as dependências do Python:
   ```bash
   pip install flask flask-cors face_recognition
   ```
   *(Nota: Usuários de Windows podem precisar do CMake e do C++ Build Tools, conforme detalhado acima).*

3. Inicie o servidor Back-end:
   ```bash
   python app.py
   ```

4. Com o servidor rodando, abra o arquivo `index.html` diretamente no seu navegador.
5. Selecione duas fotos com rostos visíveis e clique em "Verificar Identidade".