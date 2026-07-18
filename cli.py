import typer
from rich.console import Console
from rich.table import Table
from app.scanner import scan_directory
from app.parser import parse_file
from app.embeddings import (create_embeddings,create_single_embedding)
from app.vector_store import (store_documents,search_memory)
from app.ai import generate_answer

app = typer.Typer(name="devmemory", help="DevMemory AI - Your AI coding memory")
console = Console()

@app.command()
def hello():
    console.print("DevMemory AI is running!", style="bold Blue")

@app.command()
def index(path: str):
    """
    Index a project.
    """
    console.print(f"\n🔍 Scanning: {path}",style="yellow")

    files = scan_directory(path)

    if not files:

        console.print("❌ No files found",style="red" )
        return
    
    table = Table(title="Code Files")
    table.add_column("Program Files")
    table.add_column("Languages used")

    for file in files:
        table.add_row(file["path"],file["language"])
    console.print(table)

    documents = []
    console.print("\n🧩 Parsing files...",style="Green")

    for file in files:
        documents.extend(parse_file(file))

    console.print(
        f"📄 Chunks: {len(documents)}", style="Red" )
    
    texts = [ doc["content"] for doc in documents ]
    console.print( "\n Creating embeddings...", style="yellow" )
    embeddings = create_embeddings(texts )



    console.print("\nSaving vector memory...", style="yellow")

    store_documents(documents,embeddings )


    console.print("\n✅ Project memory saved!",style="bold green")



@app.command()
def ask(question: str):
    """
    Ask questions about your code.
    """
    console.print("\n🔎 Searching memory...", style="yellow")

    query_embedding = create_single_embedding(question )
    results = search_memory(query_embedding )

    documents = results["documents"][0]
    if not documents:
        console.print("❌ No matching code found",style="red" )
        return
    context = ""

    for i, doc in enumerate(documents):
        metadata = results["metadatas"][0][i]
        context += f"""

File:
{metadata['file']}

Language:
{metadata['language']}

Code:
{doc}

--------------------

"""
    console.print( "\n🤖 Asking OLAMA...", style="yellow" )
    answer = generate_answer(context,question)
    console.print("\nDevMemory AI:\n", style="bold green")
    console.print(answer)

if __name__ == "__main__":
    app()