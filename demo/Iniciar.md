# Iniciar a apicação backend

### 1️⃣ crie o ambiente de desenvolvimento

```shell
python -m venv .venv
```
### 2️⃣ inicie o ambiente
```shell
.venv\Scripts\activate
```

### 3️⃣ instale as dependencias
```shell
pip install -r requirements.txt --upgrade  
```

### 4️⃣ localize a IA

Modifique a [localização](./flaskr/yolo.py#L20) de onde está o modelo de IA

### 5️⃣ inicie a aplicação

```bash
flask --app flaskr run --debug
```
### ✅ acesse a aplicação disponível em [http://localhost:5000](http://localhost:5000).

---  

Lista de dependências instaladas:

* **[blinker](https://pypi.org/project/blinker/)**: Biblioteca para sinais.
* **[certifi](https://pypi.org/project/certifi/)**: Certificados SSL.
* **[charset-normalizer](https://pypi.org/project/charset-normalizer/)**: Biblioteca para normalização de charset.
* **[click](https://palletsprojects.com/p/click/)**: Biblioteca para criar interfaces de linha de comando.
* **[colorama](https://pypi.org/project/colorama/)**: Suporte de cores cross-platform para o terminal.
* **[contourpy](https://pypi.org/project/contourpy/)**: Geração de contornos.
* **[cycler](https://pypi.org/project/cycler/)**: Ferramenta para criar ciclos de cores.
* **[filelock](https://pypi.org/project/filelock/)**: Biblioteca para gerenciamento de bloqueios de arquivo.
* **[Flask](https://flask.palletsprojects.com/)**: Framework web.
* **[fonttools](https://pypi.org/project/fonttools/)**: Biblioteca para manipulação de fontes.
* **[fsspec](https://pypi.org/project/fsspec/)**: Interface de sistema de arquivos.
* **[gitdb](https://pypi.org/project/gitdb/)**: Banco de dados para Git.
* **[GitPython](https://gitpython.readthedocs.io/)**: Interface Python para Git.
* **[greenlet](https://pypi.org/project/greenlet/)**: Construto de concorrência leve.
* **[idna](https://pypi.org/project/idna/)**: Suporte para nomes de domínio internacionalizados.
* **[itsdangerous](https://pypi.org/project/itsdangerous/)**: Assinatura de dados confiável.
* **[Jinja2](https://jinja.palletsprojects.com/)**: Template engine.
* **[jsonify](https://pypi.org/project/jsonify/)**: Biblioteca para serialização JSON.
* **[kiwisolver](https://pypi.org/project/kiwisolver/)**: Solução de restrições algébricas.
* **[MarkupSafe](https://pypi.org/project/MarkupSafe/)**: Escapamento de strings.
* **[matplotlib](https://matplotlib.org/)**: Biblioteca de visualização de dados.
* **[mpmath](https://pypi.org/project/mpmath/)**: Aritmética de ponto flutuante multiprecisão.
* **[networkx](https://networkx.org/)**: Biblioteca para gráficos e redes.
* **[numpy](https://numpy.org/)**: Computação numérica.
* **[opencv-python](https://pypi.org/project/opencv-python/)**: Computação e manipulação de visão computacional.
* **[packaging](https://pypi.org/project/packaging/)**: Biblioteca para análise de pacotes.
* **[pandas](https://pandas.pydata.org/)**: Análise e manipulação de dados.
* **[pillow](https://pillow.readthedocs.io/)**: Manipulação de imagens.
* **[playwright](https://playwright.dev/python/)**: Automação de navegadores web.
* **[psutil](https://pypi.org/project/psutil/)**: Gerenciamento de processos e informações do sistema.
* **[py-cpuinfo](https://pypi.org/project/py-cpuinfo/)**: Informações sobre a CPU.
* **[pyee](https://pypi.org/project/pyee/)**: Implementação de eventos estilo Node.js.
* **[pyparsing](https://pypi.org/project/pyparsing/)**: Biblioteca de análise de strings.
* **[python-dateutil](https://pypi.org/project/python-dateutil/)**: Manipulação avançada de datas.
* **[pytz](https://pypi.org/project/pytz/)**: Suporte para fusos horários.
* **[PyYAML](https://pypi.org/project/PyYAML/)**: Leitura e escrita de arquivos YAML.
* **[requests](https://docs.python-requests.org/)**: Requisições HTTP.
* **[scipy](https://scipy.org/)**: Computação científica.
* **[seaborn](https://seaborn.pydata.org/)**: Visualização estatística de dados.
* **[setuptools](https://pypi.org/project/setuptools/)**: Configuração de pacotes Python.
* **[six](https://pypi.org/project/six/)**: Compatibilidade entre Python 2 e 3.
* **[smmap](https://pypi.org/project/smmap/)**: Mapeamento de streams para memória.
* **[sympy](https://www.sympy.org/)**: Matemática simbólica.
* **[torch](https://pytorch.org/)**: Machine Learning.
* **[torchvision](https://pytorch.org/vision/stable/index.html)**: Modelos e transformações de visão computacional.
* **[tqdm](https://tqdm.github.io/)**: Barras de progresso.
* **[typing\_extensions](https://pypi.org/project/typing-extensions/)**: Extensões para o módulo typing.
* **[tzdata](https://pypi.org/project/tzdata/)**: Banco de dados de fusos horários.
* **[ultralytics](https://ultralytics.com/)**: Framework de visão computacional.
* **[ultralytics-thop](https://pypi.org/project/ultralytics-thop/)**: Avaliação de desempenho de modelos de aprendizado profundo.
* **[urllib3](https://urllib3.readthedocs.io/)**: Cliente HTTP.
* **[Werkzeug](https://palletsprojects.com/p/werkzeug/)**: Biblioteca WSGI para aplicações web.
* **[reportlab](https://www.reportlab.com/)** Ferramenta poderosa para gerar documentos PDF complexos.

#### Modo de Desenvolvimento

Inicie o servidor Flask localmente com:

```bash
flask run
```


#### Modo de Produção e Deploy

Para deploy, use um servidor como [Gunicorn](https://gunicorn.org/) e um web server como Nginx. Exemplo com Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```