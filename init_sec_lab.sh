#!/usr/bin/env bash
set -e
cd ~/sec-lab || { echo "No existe ~/sec-lab"; exit 1; }

# estructura
mkdir -p scripts writeups docs vm-images

# .gitignore básico
cat > .gitignore <<'GI'
# python
__pycache__/
*.pyc
env/
venv/
secenv/
# macOS
.DS_Store
# secrets
*.pem
*.key
# node
node_modules/
GI

# primer writeup (Bandit - OverTheWire nivel 0)
TODAY=$(date +%F)
cat > "writeups/${TODAY}-bandit-nivel-0.md" <<'MD'
# Bandit — Nivel 0
- **Fecha:** $(date)
- **Scope:** OverTheWire - Bandit (nivel 0)
- **Objetivo:** Familiarizarse con SSH y comandos básicos de Linux.
- **Pasos realizados:**
  1. Crear cuenta en overthewire.org (Try OverTheWire → Bandit).
  2. Conectar por SSH: `ssh bandit0@bandit.labs.overthewire.org -p 2220` (usa credenciales del site).
  3. ...
- **Evidencias:**
  - Capturas/outputs guardados en `/writeups/assets/`
- **Aprendizajes / notas:**
  - Comandos útiles: `ls -la`, `cat`, `ssh`, `scp`, `pwd`
MD

# añade al repo y commitea
git add . 
git commit -m "chore: estructura inicial sec-lab + primer writeup Bandit"
git push -u origin main || git push
echo "Init completo. Carpetas creadas y commit push intentado."
