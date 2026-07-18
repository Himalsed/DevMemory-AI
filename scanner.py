from pathlib import Path

SUPPORTED_EXTENSIONS = {

    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".java": "Java",
    ".cpp": "C++",
    ".c": "C",
    ".html": "HTML",
    ".css": "CSS",
    ".md": "Markdown",
    ".sql": "SQL"
}

IGNORE_DIRS = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__"
}



def scan_directory(folder):
   
    files = []
    path = Path(folder)

    for file in path.rglob("*"):


        if any(
            folder in file.parts
            for folder in IGNORE_DIRS
        ):
            continue

        if (
            file.is_file()
            and file.suffix in SUPPORTED_EXTENSIONS
        ):
            files.append({ "path": str(file), "language": SUPPORTED_EXTENSIONS[file.suffix]   })
            
    return files