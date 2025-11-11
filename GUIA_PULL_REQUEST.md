# Guía: Cómo hacer un Pull Request

## Paso 1: Crear una nueva rama

Nunca hagas un Pull Request directamente desde `master`. Crea una rama nueva para tus cambios:

```bash
git checkout -b nombre-de-tu-rama
```

Ejemplo:
```bash
git checkout -b feature/mejoras-sistema-saludos
```

## Paso 2: Agregar y hacer commit de tus cambios

```bash
# Ver qué archivos has modificado
git status

# Agregar los archivos que quieres incluir en el commit
git add .gitignore
# o para agregar todos los cambios:
git add .

# Hacer commit con un mensaje descriptivo
git commit -m "Descripción clara de los cambios"
```

## Paso 3: Subir la rama al repositorio remoto

```bash
git push origin nombre-de-tu-rama
```

Si es la primera vez que subes esta rama:
```bash
git push -u origin nombre-de-tu-rama
```

## Paso 4: Crear el Pull Request en GitHub

1. Ve a tu repositorio en GitHub: https://github.com/jonareyes/sec-lab
2. Verás un banner que dice "Compare & pull request" - haz clic ahí
3. O ve a la pestaña "Pull requests" y haz clic en "New pull request"
4. Selecciona:
   - Base: `master` (rama a la que quieres fusionar)
   - Compare: `tu-rama` (tu rama con los cambios)
5. Completa el título y descripción del PR
6. Haz clic en "Create pull request"

## Comandos rápidos (resumen)

```bash
# 1. Crear y cambiar a nueva rama
git checkout -b feature/mis-cambios

# 2. Agregar cambios
git add .

# 3. Hacer commit
git commit -m "Mensaje descriptivo"

# 4. Subir al remoto
git push -u origin feature/mis-cambios

# 5. Ir a GitHub y crear el PR desde la interfaz web
```

## Buenas prácticas

- ✅ Usa nombres descriptivos para las ramas: `feature/`, `fix/`, `docs/`
- ✅ Escribe mensajes de commit claros y descriptivos
- ✅ Un PR debe tener un propósito claro y cambios relacionados
- ✅ Revisa tus cambios antes de crear el PR
- ✅ Mantén tus ramas actualizadas con `master`

## Actualizar tu rama con cambios de master

Si `master` ha cambiado mientras trabajas en tu rama:

```bash
# Cambiar a master
git checkout master

# Actualizar master
git pull origin master

# Volver a tu rama
git checkout tu-rama

# Fusionar los cambios de master en tu rama
git merge master
# o usar rebase (más limpio):
git rebase master
```

