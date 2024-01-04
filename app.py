from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def apply_styles(pdf, css_file):
    with open(css_file, 'r') as css:
        pdf.setFont("Arial", 12)
        pdf.setFillColorRGB(0, 0, 0.8)

        for line in css.readlines():
            pdf.drawString(100, pdf._pagesize[1] - 50, line.strip())

# Definindo o tamanho da página
width, height = letter

# Criando um arquivo PDF
pdf_filename = "arquivo_estilizado.pdf"
pdf = canvas.Canvas(pdf_filename, pagesize=letter)

# Adicionando uma fonte TrueType
pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))  # Substitua 'arial.ttf' pelo caminho da sua fonte TrueType

# Carregando estilos do arquivo CSS
css_file = "css/style.css"
apply_styles(pdf, css_file)

# Adicionando texto ao PDF
pdf.drawString(100, height - 100, "Este é um parágrafo com estilo CSS.")

# Salvando o PDF
pdf.save()
