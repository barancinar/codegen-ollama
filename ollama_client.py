import requests

def ask_ollama(prompt):
    system_prompt = (
        "Sen bir Python yazılım mühendisisin. Kullanıcının isteğine göre "
        "Job sınıfını temel alarak detaylandırılmış bir Python kodu üret ve bu kodu anlatan kısa bir başlık ver. "
        "Cevabın formatı şöyle olsun:\n\n"
        "Title: <başlık>\n\n```python\n<kod>\n```\n"
    )

    data = {
        "model": "llama3",  
        "prompt": f"{system_prompt}\n\n{prompt}",
        "stream": False           # Stream True yaparsan Flask tarafında stream desteği eklemelisin
    }

    # response = requests.post("http://ollama-service:11434/api/generate", json=data)
    response = requests.post("http://localhost:11434/api/generate", json=data)
    return response.json()["response"]

    