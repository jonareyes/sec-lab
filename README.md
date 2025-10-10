
## Propósito
Repositorio personal para documentar y practicar seguridad informática de forma ética:
- Labs en local (Docker / UTM)
- Scripts útiles (Python / Bash)
- Writeups y reportes (formato profesional)
- Checklist y progresos hacia certificaciones (eJPT / OSCP)

## Reglas de uso (importante)
- SOLO atacar máquinas que controlas o plataformas autorizadas (TryHackMe, HTB, VMs locales).
- No publicar exploits ni datos sensibles de terceros.
- Mantener snapshots de VMs antes de experimentar.

## Estructura del repo
- `/scripts`  — scripts utilitarios (setup, parsing, recon)
- `/writeups` — writeups en formato Markdown por lab/fecha
- `/vm-images` — instrucciones y enlaces para VMs (no subir imágenes)
- `/docs` — cheatsheets, notas de estudio, guías rápidas
- `README.md` — este archivo

## Objetivos del primer mes
1. Semana 0 — Preparación: entorno (Docker, Python, VSCode, git).  
2. Semana 1 — Fundamentos de redes y Bandit (OverTheWire).  
3. Semana 2 — Linux: comandos, permisos, journaling.  
4. Semana 3 — Python/Bash para seguridad: scripts básicos.

## Horario sugerido (3–4 horas entre semana)
- 15–20 min lectura teórica
- 90–120 min hands-on en lab
- 30–45 min scripting/documentación
- 15–30 min commit + push de resultados

## Plantilla rápida para writeups (usa en /writeups/<fecha>-<lab>.md)
- **Nombre del lab:**  
- **Fecha:**  
- **Scope:** (p. ej. `VM local: 192.168.56.101`)  
- **Herramientas usadas:** (nmap, burp, python, etc.)  
- **Pasos realizados:** (recon, enumeración, explotación)  
- **Evidencias:** (capturas de pantalla/outputs)  
- **Mitigación recomendada:**  
- **Notas / aprendizajes:**

## Cómo contribuir a este repo (mi workflow)
1. Hacer cambios / añadir scripts en rama feature.
2. `git add` → `git commit -m "feat: ..."` → `git push`
3. Mantener `main` limpio como historial de entregables.

## Contacto / notas
- Mantén siempre evidencia en local y no publiques credenciales.
- Añade aquí tus metas de certificación y links a tus perfiles (TryHackMe, HTB, GitHub).

# sec-lab
