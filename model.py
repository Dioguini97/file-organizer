import ollama

CATEGORIES = ["Trabalho", "Pessoal", "Estudos", "Desporto"]


def classify(text):
    prompt = f"""
    És um classificador de ficheiros.

    Categorias possíveis:
    - Desporto (artigos desportivos, planos de treino, relatorios de jogo, informação de atletas)
    - Trabalho (documentos profissionais, CV, contratos)
    - Pessoal (cartas, notas pessoais, faturas, recibos, pagamentos)
    - Estudos (resumos, apontamentos, livros)

    Regras:
    - Escolhe apenas UMA categoria
    - Responde só com o nome exato

    Texto:
    {text[:2000]}
    """

    response = ollama.chat(
        model='llama3',
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content'].strip()