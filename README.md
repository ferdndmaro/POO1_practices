import os

# Configuración
REPO_NAME = "POO1_practices"
HEADER = f"""# 📂 {POO1_practices}

## 🐍 Archivos Python
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(HEADER)
    for file in os.listdir():
        if file.endswith(".py"):
            f.write(f"- [{file}](./{file})\n")