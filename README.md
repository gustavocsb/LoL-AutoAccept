# League of Legends Auto Accept :video_game:

LoL Auto Accept é um aplicativo Python que se conecta à API do League of Legends para aceitar automaticamente o matchmaking.

# :hammer_and_wrench: Instalação

Para instalar e executar este projeto, você precisará seguir estas etapas:

### Clone o repositório
git clone https://github.com/gustavocsb/LoL-AutoAccept.git

### Entre no diretório do projeto
cd LoL-AutoAccept

### Instale as dependências
pip install -r requirements.txt

# :gear: Uso
Para usar este aplicativo, execute o seguinte comando:

python auto-accept.py
ou compile-o usando PyInstaller
pyinstaller --onefile --noconsole --icon=./qiydisc_1.ico auto-accept.py

# :books: Bibliotecas Utilizadas
Este projeto faz uso das seguintes bibliotecas:

lcu_driver: Usada para conectar com a API do League of Legends.
PyQt5: Usada para criar a interface gráfica do usuário.
threading: Usada para executar a GUI e a conexão com a API em threads diferentes.
os: Usada para fechar os processos do aplicativo.

# :handshake: Contribuição
Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

# :scroll: Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Espero que isso ajude! Se você tiver alguma dúvida ou precisar de mais assistência, por favor, entre em contato.
