import re
import os

def remove_stopwords(text, stopwords):
    removed_stopwords_list = []
    for stopword in stopwords:
        pattern = r'\b' + re.escape(stopword) + r'\b'
        if re.search(pattern, text, flags=re.IGNORECASE):
            text = re.sub(pattern, '', text, flags=re.IGNORECASE)
            removed_stopwords_list.append(stopword)
    return text, removed_stopwords_list

def process_directory(input_directory, output_directory, stopwords):
    for filename in os.listdir(input_directory):
        if filename.startswith("indice_invertido"):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)

            with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
                for line in infile:
                    removed_stopwords_line, removed_stopwords_list = remove_stopwords(line, stopwords)
                    if removed_stopwords_line.strip():  # Verificar si la línea no está vacía después de la eliminación
                        if removed_stopwords_list != [ ]:
                            print(f"Stopword removed: {', '.join(removed_stopwords_list)}")
                        outfile.write(removed_stopwords_line)

if __name__ == "__main__":
    # Carpeta de entrada y salida
    input_directory = "./"
    output_directory = "./stopwords"

    # Lista de stopwords
    stopwords = ["a", "an", "the", "this", "and", "for", "by", "at", "any", "be", "from", "us", "as", "so", "or", "but", "to", "of", "if", "is", "are", "was", "were", "I", "you", "he", "she", "it", "we", "they"]
    # Procesamiento del directorio
    process_directory(input_directory, output_directory, stopwords)

