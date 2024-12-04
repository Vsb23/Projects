import bs4 
import os 
import zipfile

def extract_epub_content(epub_path, output_folder):
    # Ottieni il nome base del file epub
    base_name = os.path.splitext(os.path.basename(epub_path))[0]
    
    # Crea una cartella per questo specifico epub
    epub_output_folder = os.path.join(output_folder, base_name)
    os.makedirs(epub_output_folder, exist_ok=True)
    
    # Rinomina temporaneamente il file in .zip
    zip_file = epub_path.replace(".epub", ".zip")
    os.rename(epub_path, zip_file)
    
    try:
        # Estrai il contenuto
        with zipfile.ZipFile(zip_file, "r") as zip_ref:
            zip_ref.extractall(epub_output_folder)
        
        # Cerca la cartella OEBPS/Text
        text_folder = os.path.join(epub_output_folder, "OEBPS", "Text")
        if os.path.exists(text_folder):
            for xhtml in os.listdir(text_folder):
                if xhtml.endswith('.xhtml') or xhtml.endswith('.html'):
                    # Crea un file di output per ogni file xhtml
                    output_file = os.path.join(epub_output_folder, f"{os.path.splitext(xhtml)[0]}.txt")
                    
                    with open(os.path.join(text_folder, xhtml), "r", encoding='utf-8') as f:
                        text = f.read()
                    
                    soup = bs4.BeautifulSoup(text, 'html.parser')
                    tags = soup.find_all(['p', 'h1', 'h2'])
                    
                    with open(output_file, "w", encoding='utf-8') as out_f:
                        for tag in tags:
                            out_f.write(tag.get_text().strip() + "\n\n")
        
        print(f"Contenuto estratto e salvato in: {epub_output_folder}")
    
    finally:
        # Rimuovi i file temporanei estratti (tranne i .txt che abbiamo creato)
        for root, dirs, files in os.walk(epub_output_folder, topdown=False):
            for name in files:
                if not name.endswith('.txt'):
                    os.remove(os.path.join(root, name))
            for name in dirs:
                try:
                    os.rmdir(os.path.join(root, name))
                except OSError:
                    pass  # La cartella potrebbe non essere vuota, la ignoriamo
        
        # Rinomina il file zip di nuovo in epub
        os.rename(zip_file, epub_path)

# Cartella contenente i file EPUB
path = "C:\\Users\\stefa\\Desktop"
output_folder = "C:\\Users\\stefa\\Desktop\\EPUB_Extracted"

# Assicurati che la cartella di output principale esista
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(path):
    if file.endswith(".epub"):
        epub_path = os.path.join(path, file)
        extract_epub_content(epub_path, output_folder)