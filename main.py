import os
import shutil
import sys
from pathlib import Path

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".zip", ".rar", ".tar", ".gz"],
    "Vídeos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Música": [".mp3", ".wav", ".aac", ".flac"]
}

MAIN_PATH = Path('C:\\Users\diogo')

def organize_files(folder_path: str):
    folder = Path(folder_path)

    if not folder.exists():
        print(f'Erro: A pasta {folder} não existe.')
        return

    for item in folder.iterdir():
        if item.is_file():
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if item.suffix.lower() in extensions:
                    category_folder = MAIN_PATH / category
                    category_folder.mkdir(exist_ok=True)
                    shutil.move(str(item), str(category_folder / item.name))
                    moved = True
                    break
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