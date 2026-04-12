# 🚀 Sistema de Login Flask & Bootstrap

Este é um projeto de uma página de login moderna e responsiva, desenvolvida utilizando o framework **Flask** (Python) no backend e **Bootstrap 5** com variáveis personalizadas de CSS no frontend.

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3.x + Flask
* **Frontend:** HTML5, CSS3 (Custom Properties), Bootstrap 5
* **Arquitetura:** Application Factory Pattern (`create_app`)

## 🎨 Funcionalidades do Design

* **Variáveis CSS:** Sistema de cores baseado em `--cor-primaria` e `--cor-secundaria`, facilitando a troca de temas.
* **Responsividade:** Adaptável a qualquer tamanho de tela (Mobile, Tablet e Desktop).
* **Interface Moderna:** Cards com sombras suaves, gradientes e efeitos de hover nos botões.

## 📂 Estrutura do Projeto

```text
meu_projeto/
├── app/
│   ├── __init__.py      # Contém a função create_app()
│   ├── static/          # Arquivos CSS, Imagens e JS
│   │   └── style.css    # CSS com variáveis primárias/secundárias
│   │─── templates/      # Páginas HTML (index.html)
│   └── main.py          # Ponto de entrada da aplicação
├── run.py              # Ponto de execução da aplicação
└── README.md
```

# 🚀 Como Executar o Projeto
 Clone o repositório:
```Bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
Crie um ambiente virtual e instale o Flask:
```

```Bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Mac/Linux:
source venv/bin/activate
```

## Inicie o Servidor:
```Bash
pip install flask
Inicie o servidor:
python run.py
```
## Acesse no navegador:
```Bash
http://127.0.0.1:5000
```