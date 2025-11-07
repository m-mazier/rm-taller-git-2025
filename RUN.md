# Guía de Ejecución (RUN.md)

Este archivo describe cómo "ejecutar" o interactuar con este proyecto de prueba.

## 1. Prerrequisitos

* Tener `git` instalado en tu sistema local.
* (Opcional) Una cuenta de GitHub si deseas hacer un *fork* de este proyecto.

## 2. "Ejecución" Principal

Este proyecto no tiene un software que se "ejecute" (como un servidor o una aplicación).

La "ejecución" principal consiste en interactuar con él usando Git:

1.  **Clona el repositorio:**
    ```bash
    git clone [URL_DE_TU_REPOSITORIO]
    ```

2.  **Entra al directorio:**
    ```bash
    cd [NOMBRE_DEL_DIRECTORIO]
    ```

## 3. Tareas Comunes (Simulación)

Aquí simulamos tareas de desarrollo.

### Tarea: Hacer un cambio

1.  Crea una nueva rama:
    ```bash
    git checkout -b mi-nueva-rama
    ```
2.  Modifica este archivo (`RUN.md`) o el `README.md` con cualquier editor de texto.
3.  Añade y confirma tus cambios:
    ```bash
    git add .
    git commit -m "feat: Se agrega mi primer cambio de prueba"
    ```

### Tarea: Subir tus cambios

1.  Sube tu rama a GitHub:
    ```bash
    git push -u origin mi-nueva-rama
    ```

### Tarea: Actualizar tu proyecto

1.  Vuelve a la rama principal (usualmente `main` o `master`):
    ```bash
    git checkout main
    ```
2.  Trae los últimos cambios de GitHub (si alguien más subió algo):
    ```bash
    git pull origin main
    ```