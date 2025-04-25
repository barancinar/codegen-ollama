import re

def parse_response(response_text):
    title_match = re.search(r"Title:\s*(.*)", response_text)
    code_match = re.search(r"```python(.*?)```", response_text, re.DOTALL)

    title = title_match.group(1).strip() if title_match else "Başlık bulunamadı"
    code = code_match.group(1).strip() if code_match else "Kod bulunamadı"

    return title, code
