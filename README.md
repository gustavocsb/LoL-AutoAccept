# League of Legends Auto Accept :video_game:

LoL Auto Accept é um aplicativo Python que se conecta à API do League of Legends para aceitar automaticamente o matchmaking.<br><br>


# :hammer_and_wrench: Instalação
### Instale o Python
Este projeto requer Python 3.11.5. Se você ainda não tem o Python instalado, siga estas etapas:

1. Baixe a versão mais recente do Python em https://www.python.org/downloads/.
2. Execute o instalador e siga as instruções na tela.
3. Verifique se o Python foi instalado corretamente executando o seguinte comando no terminal:<br><br>
python --version<br><br>
Você deve ver Python 3.11.5 como resposta.<br><br>

### Clone o repositório
git clone https://github.com/gustavocsb/LoL-AutoAccept.git<br><br>

### Entre no diretório do projeto
cd LoL-AutoAccept<br><br>

### Instale as dependências
pip install -r requirements.txt<br><br>

# :gear: Uso
Para usar este aplicativo, execute o seguinte comando:

python auto-accept.py<br><br>
ou compile-o usando PyInstaller<br><br>
pyinstaller --onefile --noconsole --icon=./qiydisc_1.ico auto-accept.py<br><br>

# :books: Bibliotecas Utilizadas
Este projeto faz uso das seguintes bibliotecas:

lcu_driver: Usada para conectar com a API do League of Legends.<br>
PyQt5: Usada para criar a interface gráfica do usuário.<br>
threading: Usada para executar a GUI e a conexão com a API em threads diferentes.<br>
os: Usada para fechar os processos do aplicativo.<br><br>

# :handshake: Contribuição
Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.<br><br>

# :scroll: Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.<br><br>

Espero que isso ajude! Se você tiver alguma dúvida ou precisar de mais assistência, por favor, entre em contato.
