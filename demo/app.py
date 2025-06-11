from flask import Flask, request, jsonify
from PIL import Image
import os
import numpy as np
import cv2
import uuid
from ultralytics import YOLO
from detection import Detection
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Carrega o modelo treinado
model = YOLO(model = r"C:\study-space\python-ia\dog-detect\yolov5su.pt")#"best.pt")  # Substitua por seu caminho se necessário

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

detection = Detection()

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'Nenhuma parte do arquivo', 400

    file = request.files['image']
    if file.filename == '':
        return 'Nenhum arquivo selecionado', 400

    
    if file:
        # Gera nome único para o arquivo
        filename = f"{uuid.uuid4().hex}.jpg"
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        img = Image.open(file_path).convert("RGB")
        img = np.array(img)
        img = cv2.resize(img, (512, 512))

        detected_classes = detection.detect_from_image(img)

        os.remove(file_path)

        # Retornar apenas a primeira detecção, se houver
        if detected_classes:
            first_detection = detected_classes[0]
            return {"detected_class": first_detection}, 200
        else:
            return {"message": "Nenhum objeto detectado"}, 200



@app.route('/')
def apifuncionando():
    return "A aplicação está em funcionamento 🤲"

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import datetime

def generate_medical_report(filename):
    # Cria o documento
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    # Estilos
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=18,
        leading=22,
        alignment=1,
        textColor=colors.darkblue
    )
    section_title_style = ParagraphStyle(
        'SectionTitleStyle',
        parent=styles['Heading2'],
        fontSize=14,
        leading=18,
        textColor=colors.darkred
    )
    normal_style = styles['Normal']

    # Título
    elements.append(Paragraph("Prontuário Médico", title_style))
    elements.append(Spacer(1, 20))

    # Informações do paciente
    patient_info = [
        ["Nome do Paciente:", "João da Silva"],
        ["Data de Nascimento:", "12/06/1985"],
        ["Data do Relatório:", datetime.datetime.now().strftime("%d/%m/%Y")],
        ["Médico Responsável:", "Dra. Maria Oliveira"]
    ]
    table = Table(patient_info, colWidths=[150, 300])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
    ]))
    elements.append(table)
    elements.append(Spacer(1, 20))

    # Seção: Diagnóstico
    elements.append(Paragraph("Diagnóstico", section_title_style))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(
        "O exame de imagem de raio-X cerebral revelou a presença de um tumor localizado na hipófise. "
        "Esse tipo de tumor, geralmente benigno, pode causar sintomas relacionados à visão, alterações hormonais, e dores de cabeça frequentes.",
        normal_style
    ))
    elements.append(Spacer(1, 20))

    # Seção: Cuidados e Procedimentos
    elements.append(Paragraph("Cuidados e Procedimentos Recomendados", section_title_style))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(
        "1. Consulta com um endocrinologista para avaliação dos níveis hormonais.\n"
        "2. Agendamento de ressonância magnética para avaliação detalhada.\n"
        "3. Monitoramento regular com exames de sangue e acompanhamento médico.\n"
        "4. Caso necessário, considerar tratamento cirúrgico ou medicamentoso, conforme orientação médica.",
        normal_style
    ))
    elements.append(Spacer(1, 20))

    # Seção: Informações Adicionais
    elements.append(Paragraph("Informações Adicionais", section_title_style))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(
        "Este relatório é apenas uma avaliação inicial e não substitui a consulta com um médico especialista. "
        "Em caso de dúvidas ou agravamento dos sintomas, procure atendimento médico imediatamente.",
        normal_style
    ))

    # Gera o PDF
    doc.build(elements)
    print(f"Relatório gerado: {filename}")

# Gera o relatório
generate_medical_report("prontuario_medico.pdf")

if __name__ == '__main__':
    app.run(debug=True)
