import shutil
import sys
from pathlib import Path
from PIL import Image
from PyPDF2 import PdfReader
import pytesseract
from model import classify

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".zip", ".rar", ".tar", ".gz"],
    "Vídeos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Música": [".mp3", ".wav", ".aac", ".flac"]
}

MAIN_PATH = Path('C:\\Users\\diogo\\Documents')


def extract_content(file_path: Path):
    suffix = file_path.suffix.lower()

    try:
        # .txt
        if suffix == '.txt':
            return file_path.read_text(encoding='utf-8', errors='ignore')

        # .pdf
        elif suffix == '.pdf':
            reader = PdfReader(file_path)
            return ' '.join([p.extract_text() or '' for p in reader.pages])

        # .docx
        # elif suffix == ".docx":
        #     doc = newdocument(file_path)
        #     return "\n".join([p.text for p in doc.paragraphs])

        # IMAGENS (OCR)
        elif suffix in [".jpg", ".png", ".jpeg"]:
            return pytesseract.image_to_string(Image.open(file_path))

        # OUTROS (fallback)
        else:
            return ""


    except Exception as e:
        print(f'Erro: Não foi possivel ler o conteudo do file {file_path}\n {e}')


def organize_files(folder_path: str):
    folder = Path(folder_path)

    if not folder.exists():
        print(f'Erro: A pasta {folder} não existe.')
        return

    for item in folder.iterdir():
        moved = False
        if item.is_file():
            text = extract_content(item)
            category = classify(text)
            category_folder = MAIN_PATH / category
            category_folder.mkdir(exist_ok=True)
            shutil.move(str(item), str(category_folder / item.name))
            moved = True
        if not moved:
            others_folder = MAIN_PATH / 'Others'
            others_folder.mkdir(exist_ok=True)
            shutil.move(str(item), str(others_folder / item.name))

    print("Organização Concluida!")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python organize_files.py /caminho/para/pasta")
    else:
        organize_files(sys.argv[1])
