# AI Code Generator with Ollama

This project is a web application that generates Python code using the Ollama AI model. 
It provides a simple interface where users can describe their code requirements and get AI-generated Python code in response.

## 🚀 Features

- AI-powered code generation
- Clean and modern web interface
- Real-time code highlighting
- Copy code functionality
- Responsive design
- Docker and Kubernetes support

## 🛠️ Technologies

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Bootstrap 5
- **AI Model**: Ollama (llama2)
- **Container**: Docker
- **Orchestration**: Kubernetes (Minikube)
- **Code Highlighting**: PrismJS

## 📋 Prerequisites

- Python 3.12+
- Docker
- Minikube
- kubectl
- Ollama

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/barancinar/codegen-ollama.git
cd codegen-ollama
```

2. **Local Development Setup**
```bash
# Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## 🏗️ Project Structure

```
codegen-ollama/
├── app.py              # Flask application
├── ollama_client.py    # Ollama API client
├── utils.py           # Utility functions
├── Dockerfile         # Docker configuration
├── requirements.txt   # Python dependencies
├── deployment.yaml    # Kubernetes deployment for webapp
├── ollama-deployment.yaml # Kubernetes deployment for Ollama
├── static/
│   ├── css/
│   └── js/
└── templates/
    ├── index.html    # Main page
    ├── navbar.html   # Navigation component
    ├── features.html # Features component
    └── footer.html   # Footer component
```

## 🌟 Usage

1. Access the application through your browser
2. Enter your code requirements in the text area
3. Click "Kod Üret" (Generate Code)
4. View the generated code with syntax highlighting
5. Copy the code using the copy button

## 🔍 API Endpoints

- `GET /`: Main page
- `POST /`: Generate code endpoint

## 🤝 Acknowledgments

- [Ollama](https://ollama.ai/) for the AI model
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Bootstrap](https://getbootstrap.com/) for the UI components
- [PrismJS](https://prismjs.com/) for code highlighting

## ✨ Author

Baran Çınar
- GitHub: [@barancinar](https://github.com/barancinar)
