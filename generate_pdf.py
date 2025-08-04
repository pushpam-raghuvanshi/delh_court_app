from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_case_pdf(case_data):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, height - 50, "Delhi High Court - Case Summary")

    pdf.setFont("Helvetica", 12)
    y = height - 100
    line_spacing = 20

    for key, value in case_data.items():
        pdf.drawString(50, y, f"{key.replace('_', ' ').title()}: {value}")
        y -= line_spacing

    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return buffer
