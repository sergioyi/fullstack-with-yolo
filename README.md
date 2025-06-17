# **Reconhecimento de Tumores Cerebrais com YOLO**

Este projeto apresenta um sistema de apoio ao diagnóstico médico para a detecção e classificação de tumores cerebrais em imagens de tomografia computadorizada. Utilizando a arquitetura YOLO, o sistema identifica diferentes tipos de tumores em tempo real e gera relatórios para auxiliar profissionais da saúde na tomada de decisões rápidas e eficazes.

---

## **Funcionalidades**
- Detecção de tumores em imagens de tomografia computadorizada.
- Classificação em 4 categorias:
  - Glioma Tumor
  - Meningioma Tumor
  - Pituitary Tumor
  - No Tumor
- Geração de relatórios médicos em PDF.
- Processamento em tempo real.

---

## **Arquitetura**
A arquitetura do sistema é baseada no modelo **YOLO** (You Only Look Once) para detecção de objetos, treinado com um dataset de tumores cerebrais. O sistema é dividido em:
1. **Backend**: Implementado em Flask para gerenciar uploads de imagens, processamento, e geração de relatórios.
2. **Frontend**: Desenvolvido em React.js para uma interface de usuário intuitiva.
3. **YOLO Model**: Treinado com imagens pré-processadas, utilizando técnicas de transferência de aprendizado.

---

## **Pré-requisitos**
- Python 3.8 ou superior
- Node.js 16 ou superior
- Bibliotecas Python:
  - `ultralytics`
  - `opencv-python`
  - `pillow`
  - `numpy`
  - `flask`
