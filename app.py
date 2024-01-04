from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Definindo o tamanho da página
width, height = letter

# Criando um arquivo PDF
pdf_filename = "arquivo_estilizado.pdf"
pdf = canvas.Canvas(pdf_filename, pagesize=letter)

# Adicionando uma fonte TrueType
pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))  # Substitua 'arial.ttf' pelo caminho da sua fonte TrueType

# Adicionando texto ao PDF com estilo CSS
css = """
    body {
        font-family: Arial, sans-serif;
        font-size: 12px;
        color: #333333;
    }

    h1 {
        font-size: 18px;
        color: #0066cc;
    }

    .highlight {
        background-color: #ffff99;
    }
"""

# Aplicando estilos usando o ReportLab
pdf.setFont("Arial", 12)
pdf.setFillColorRGB(0, 0, 0.8)
pdf.drawString(100, height - 50, "Exemplo de PDF Estilizado")

# Adicionando uma caixa de texto com classe CSS
text_object = pdf.beginText(100, height - 150)
text_object.setFont("Arial", 12)
text_object.setTextOrigin(100, height - 150)
text_object.setFillColorRGB(0, 0, 0.8)
text_object.textLine("Texto destacado com classe CSS.")
pdf.drawText(text_object)

# Salvando o PDF
pdf.save()
