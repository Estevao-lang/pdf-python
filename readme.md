README
Arquivo Estilizado PDF com ReportLab
Este é um exemplo simples de como criar um arquivo PDF estilizado usando a biblioteca ReportLab em Python. O script gera um PDF contendo texto formatado com base em um estilo definido em um bloco de CSS.

Requisitos
Certifique-se de ter Python instalado em seu sistema. Você pode instalar as dependências necessárias usando o seguinte comando:

pip install reportlab chardet
Isso garantirá que ambos os pacotes reportlab e chardet estejam instalados antes de executar o script. Agradeço por apontar esse detalhe, e espero que isso seja útil para quem estiver utilizando seu script.


Executando o Script
Baixe o script app.py para o seu sistema.

Execute o script utilizando o seguinte comando:



python app.py
O script criará um arquivo PDF chamado arquivo_estilizado.pdf no mesmo diretório.

Personalização
Fonte TrueType: Você pode substituir 'arial.ttf' pelo caminho da sua fonte TrueType desejada.

Estilos CSS: Os estilos são definidos dentro do bloco de texto css. Você pode personalizar as propriedades CSS conforme necessário.

Arquivos Adicionais
O exemplo inclui um arquivo styles.css separado, onde você pode definir os estilos CSS de maneira mais organizada. O arquivo styles.css é carregado no script para aplicar os estilos ao PDF.

Limitações
O suporte direto para CSS em PDF é limitado. Este exemplo utiliza métodos específicos do ReportLab para adicionar estilos ao PDF, mas pode não cobrir todas as propriedades CSS.