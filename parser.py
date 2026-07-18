MAX_CHUNK_SIZE = 1000

def read_file(path):

    try:
        with open( path, "r", encoding="utf-8"  ) as file:
         return file.read()
    except:
        return None

def split_code(code):

    chunks = []
    current = ""

    for line in code.split("\n"):
        current += line + "\n"

        if len(current) >= MAX_CHUNK_SIZE:
            chunks.append(current)
            current = ""

    if current:
        chunks.append(current)
    return chunks

def parse_file(file):

    content = read_file(file["path"]  )
    if not content:
        return []
    chunks = split_code(
        content
    )
    documents = []
    for index, chunk in enumerate(chunks):

        documents.append(
            {
                "content": chunk,
                "metadata": {
                 "file": file["path"],
                    "language": file["language"],
                    "chunk": index
                }
            }
        )
    return documents