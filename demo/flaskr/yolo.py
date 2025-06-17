from flask import request, jsonify, Blueprint
from PIL import Image
import os
import numpy as np
import cv2
import uuid
from ultralytics import YOLO
from flaskr.detection import Detection
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import datetime
from flask import send_file

bp = Blueprint('yolo', __name__)


UPLOAD_FOLDER = os.path.abspath('uploads')
REPORT_FOLDER = os.path.abspath('reports')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

detection = Detection()

@bp.route('/upload', methods=['POST'])
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

@bp.route('/uploadwithpdf', methods=['POST'])
def upload_image_with_pdf():
    if 'image' not in request.files:
        return 'Nenhuma parte do arquivo', 400

    file = request.files['image']
    username = request.form.get("username")
    if file.filename == '':
        return 'Nenhum arquivo selecionado', 400

    if file:
        filename = f"{uuid.uuid4().hex}.jpg"
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        img = Image.open(file_path).convert("RGB")
        img = np.array(img)
        img = cv2.resize(img, (512, 512))

        detected_classes = detection.detect_from_image(img)
        os.remove(file_path)

        if detected_classes:
            detected_class = detected_classes[0]
            report_filename = f"report_{uuid.uuid4().hex}.pdf"
            report_path = os.path.join(REPORT_FOLDER, report_filename)
            generate_medical_report(report_path, detected_class, username=username)
            print(f"PDF gerado: {report_path}")
            # Enviar o PDF como resposta
            return send_file(report_path, as_attachment=True, download_name=report_filename)

        else:
            return {"message": "Nenhum objeto detectado"}, 200


def generate_medical_report(filename, detected_class, username):
    # Mapeamento de informações com base na classe detectada
    report_details = {
        "pituitary_tumor": {
            "diagnosis": (
                "O exame de imagem revelou a presença de um tumor localizado na hipófise. "
                "Esse tipo de tumor, geralmente benigno, pode causar sintomas relacionados à visão, alterações hormonais e dores de cabeça frequentes."
            ),
            "recommendations": [
                "Consulta com um endocrinologista para avaliação dos níveis hormonais.",
                "Agendamento de ressonância magnética para avaliação detalhada.",
                "Monitoramento regular com exames de sangue e acompanhamento médico.",
                "Considerar tratamento cirúrgico ou medicamentoso, conforme orientação médica."
            ]
        },
        "glioma_tumor": {
            "diagnosis": (
                "O exame de imagem revelou a presença de um glioma. Esse tipo de tumor afeta o sistema nervoso central e pode causar sintomas como "
                "convulsões, dores de cabeça e déficits neurológicos."
            ),
            "recommendations": [
                "Consulta com um neurocirurgião para avaliação detalhada.",
                "Realizar biópsia para confirmar o tipo exato de glioma.",
                "Considerar radioterapia ou quimioterapia, conforme indicado pelo especialista.",
                "Monitoramento regular com exames de imagem."
            ]
        },
        "meningioma_tumor": {
            "diagnosis": (
                "O exame revelou um meningioma, que é um tumor geralmente benigno, originado nas meninges. "
                "Pode causar sintomas como dores de cabeça persistentes, problemas de visão e fraqueza nos membros."
            ),
            "recommendations": [
                "Consulta com um neurocirurgião para planejar o tratamento.",
                "Agendamento de ressonância magnética para monitoramento do crescimento do tumor.",
                "Considerar cirurgia, se o tumor estiver causando compressão cerebral significativa.",
                "Avaliar necessidade de radioterapia em casos específicos."
            ]
        },
        "no_tumor": {
            "diagnosis": "Nenhum tumor foi identificado no exame de imagem. O cérebro apresenta características normais.",
            "recommendations": ["Manter acompanhamento regular e hábitos saudáveis."]
        }
    }

    # Detalhes padrão se a classe não estiver mapeada
    details = report_details.get(
        detected_class,
        {
            "diagnosis": "O exame retornou uma classe não identificada. Consulte um especialista para análise mais detalhada.",
            "recommendations": ["Consultar um médico especialista para avaliação."]
        }
    )

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
        ["Nome do Paciente:", username],
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
    elements.append(Paragraph(details["diagnosis"], normal_style))
    elements.append(Spacer(1, 20))

    # Seção: Cuidados e Procedimentos
    elements.append(Paragraph("Cuidados e Procedimentos Recomendados", section_title_style))
    elements.append(Spacer(1, 10))
    recommendations = "\n".join(f"{i + 1}. {rec}" for i, rec in enumerate(details["recommendations"]))
    elements.append(Paragraph(recommendations, normal_style))
    elements.append(Spacer(1, 20))

    # Gera o PDF
    doc.build(elements)
    print(f"Relatório gerado: {filename}")
