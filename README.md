# Práctica Final DevSecOps

Este repositorio contiene diferentes Workflows vistos a lo largo de la asignatura DevSecOps, además de los diferentes badges obtenidos.

## CI/CD Pipeline

[![CI/CD Pipeline](https://github.com/pgonzg09/DevSecOps-PracticaFinal/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/pgonzg09/DevSecOps-PracticaFinal/actions/workflows/ci-cd.yml)

Este workflow de CI/CD es el encargado de realizar las pruebas de integración y despliegue continuos, en este caso cada vez que se realiza un `push` a la rama `main` del repositorio. El código de este workflow se encuentra en el archivo [ci-cd.yml](.github/workflows/ci-cd.yml) y consta de los siguientes pasos:

1. Checkout code: utiliza [actions/checkout@v4](https://github.com/actions/checkout) para comprobar el código fuente del repositorio para que el workflow pueda acceder a él.
2. Set up Docker: utiliza [docker/setup-buildx-action@v3](https://github.com/docker/setup-buildx-action) para crear e iniciar un compilador que pueda utilizarse el los siguientes pasos del workflow.
3. Build Docker image: compila el código utilizando el Dockerfile del repositorio (`docker build -t flask-app .`).
4. Run Docker container: ejecuta el contenedor en el puerto `5000` en segundo plano (`docker run -d -p 5000:5000 flask-app`).
5. Verify Docker running containers: comprueba los contenedores activos (`docker ps`).
6. Wait util service is available: espera a que el servicio esté disponible para probar posteriormente si es accesible.
    ```bash
    for i in {1..10}; do
        curl -f http://localhost:5000 && break
        echo "Waiting for the service..."
        sleep 5
    done
    ```
7. Test the app: realiza una prueba de acceso simple mediante una petición HTTP a la app (`curl -f http://localhost:5000`).
8. Stop all containers: termina la ejecución de todos los contenedores activos (`docker stop $(docker ps -q)`).

## Pylint

[![Pylint](https://github.com/pgonzg09/DevSecOps-PracticaFinal/actions/workflows/pylint.yml/badge.svg)](https://github.com/pgonzg09/DevSecOps-PracticaFinal/actions/workflows/pylint.yml)

Este workflow realiza un análisis del código Python del repositorio utilizando la herramienta Pylint, que permite analizar el código sin la necesidad de ejecutarlo cada vez que se realiza un `push` a la rama `main` del repositorio. Pylint comprueba la existencia de errores, aplica un estándar al código, busca trazas en el código que indiquen posibles problemas, que sin ser bugs/errores, pueden ser errores de diseño y/o desarrollo que eventualmente deriven en poca calidad del código u otros problemas técnicos, y hace sugerencias para la refactorización del código. El código de este workflow se encuentra en el archivo [pylint.yml](.github/workflows/pylint.yml) y consta de los siguientes pasos:

1. Checkout code: utiliza [actions/checkout@v4](https://github.com/actions/checkout) para comprobar el código fuente del repositorio para que el workflow pueda acceder a él.
2. Set up Python: utiliza [actions/setup-python@v5](https://github.com/actions/setup-python) para establecer el entorno de Python (versión `3.9` en este caso) para poder instalar posteriormente las herramientas necesarias para analizar el código.
3. Install dependecies: instala las dependencias para realizar el análisis: pytlint, flask y autopep8.
4. Run autopep8: realiza un formateo automático para que el código este conforme con la guia de estilo PEP8.
5. Analysing the code with pylint: analiza todos los archivos Python del repositorio utilizando la herramienta Pylint.

## Doxygen

[![Doxygen](https://github.com/pgonzg09/DevSecOps-PracticaFinal/actions/workflows/doxygen.yml/badge.svg)](https://github.com/pgonzg09/DevSecOps-PracticaFinal/actions/workflows/doxygen.yml)

Este workflow genera la documentación del proyecto de forma automática utilizando la herramienta `Doxygen`, la guarda en la carpeta [docs](docs) y la despliega en la rama `gh-pages` para su visualización en Github Pages cada vez que se realiza un `push` a la rama `main` del repositorio. El código de este workflow se encuentra en el archivo [doxygen.yml](.github/workflows/doxygen.yml) y consta de los siguientes pasos:

1. Checkout code: utiliza [actions/checkout@v4](https://github.com/actions/checkout) para comprobar el código fuente del repositorio para que el workflow pueda acceder a él.
2. Generate Doxygen: genera la documentación utilizando [mattnotmitt/doxygen-action@edge](https://github.com/mattnotmitt/doxygen-action) partiendo del archivo de configuración [Doxyfile](.github/Doxyfile). Se han configurado los siguientes parámetros dentro del archivo de configuración:
    - PROJECT_NAME: especifica el nombre del proyecto. -> `"Práctica final DevSecOps"`
    - INPUT: especifica las carpetas y archivos a partir de los cuales se genera la documentación. -> `README.md \ DevSecOps-PracticaFinal`
    - FILE_PATTERNS: especifica los patrones de archivo para generar la documentación. -> ` *.md \ *.c \ *.cpp \ *.hpp \ *.py`
    - OUTPUT_DIRECTORY: especifica la carpeta donde se guardará la documentación generada. -> `docs/`
    - GENERATE_HTML: habilita/deshabilita la generación de HTML. -> `YES`
    - GENERATE_LATEX: habilita/deshabilita la generación de Latex. -> `NO`
3. Deploy Doxygen page: despliega la documentación generada con Doxygen en `gh-pages` utilizando [peaceiris/actions-gh-pages@v4](https://github.com/peaceiris/actions-gh-pages).

## Flake8

[![Flake8](https://github.com/pgonzg09/DevSecOps-PracticaFinal/actions/workflows/flake8.yml/badge.svg)](https://github.com/pgonzg09/DevSecOps-PracticaFinal/actions/workflows/flake8.yml)


Este workflow realiza un análisis estático del código Python del repositorio utilizando la herramienta `flake8`, que a su vez agrupa `pycodestyle`, `pyflakes`, `mccabe` y otra serie de plugins de terceros para comprobar el estilo y calidad del código Python, cada vez que se realiza un `push` a la rama `main` del repositorio. El código de este workflow se encuentra en el archivo [flake8.yml](.github/workflows/flake8.yml) y consta de los siguientes pasos:

1. Check out source repository: utiliza [actions/checkout@v4](https://github.com/actions/checkout) para comprobar el código fuente del repositorio para que el workflow pueda acceder a él.
2. Set up Python: utiliza [actions/setup-python@v5](https://github.com/actions/setup-python) para establecer el entorno de Python (versión `3.9` en este caso) para poder utilizar posteriormente la herramienta `flake8`.
3. Flake8 Lint: utiliza [py-actions/flake8@v2](https://github.com/py-actions/flake8) para realizar el análisis del código. A su vez, este workflow instala el paquete de Python `flake8` y ejecuta el linting lógico y de estilo.

## Codacy

[![Codacy](https://github.com/pgonzg09/DevSecOps-PracticaFinal/actions/workflows/codacy.yml/badge.svg)](https://github.com/pgonzg09/DevSecOps-PracticaFinal/actions/workflows/codacy.yml)

Este workflow realiza un análisis estático del código de Python del repositorio y subir los datos del análisis para su visualización en `Security/Code scanning` cada vez que se realiza un `push` o un `pull-request` a la rama `main` del repositorio. El código de este workflow se encuentra en el archivo [codacy.yml](.github/workflows/codacy.yml) y consta de los siguientes pasos:

1. Checkout code: utiliza [actions/checkout@v4](https://github.com/actions/checkout) para comprobar el código fuente del repositorio para que el workflow pueda acceder a él.
2. Run Codacy Analysis CLI: utiliza [codacy/codacy-analysis-cli-action@master](https://github.com/codacy/codacy-analysis-cli-action) para ejecutar el análisis estático del código del repositorio.
3. Upload SARIF results file: utiliza [github/codeql-action/upload-sarif@v3](https://github.com/github/codeql-action/blob/main/upload-sarif/action.yml) para subir los resultados (formato SARIF) del análisis al repositorio de GitHub.

## Test (with Pytest)

[![Test](https://github.com/pgonzg09/DevSecOps-PracticaFinal/actions/workflows/test.yml/badge.svg)](https://github.com/pgonzg09/DevSecOps-PracticaFinal/actions/workflows/test.yml)

Este workflow realiza varios test unitarios a la app utilizando Pytestada vez que se realiza un `push` a la rama `main` del repositorio. El código de este workflow se encuentra en el archivo [test.yml](.github/workflows/test.yml) y consta de los siguientes pasos:

1. Checkout code: utiliza [actions/checkout@v4](https://github.com/actions/checkout) para comprobar el código fuente del repositorio para que el workflow pueda acceder a él.
2. Set up Python: utiliza [actions/setup-python@v5](https://github.com/actions/setup-python) para establecer el entorno de Python (versión `3.9` en este caso) para poder utilizar posteriormente la herramienta `pytest`.
3. Install dependencies: instala las dependencias para realizar el análisis: flask y pytest.
4. Run test: lanza los test ubicados en el archivo `test.py` y los lanza utilizando `pytest`.

## Act

Act es una herramienta que permite ejecutar GitHub Actions de forma local que proporciona ciertas ventajas:

- **Retroalimentación rápida**: se puede utilizar act para ejecutar las acciones en el entorno local. Las variables de entorno y el sistema de archivos se configuran de manera que emulan el entorno proporcionado por GitHub.
- **Ejecución local de tareas**: act permite aprovechar las GitHub Actions definidas en los archivos `.github/workflows/` como reemplazo del Makefile, facilitando la gestión y automatización de tareas.

Para instalar act en nuestra máquina (requiere `Go toolchain 1.18+`):

```bash
git clone https://github.com/nektos/act.git
cd act/
make build
```

Para utilizar act en nuestra máquina bastará con utilizar el siguiente comando:

```bash
act
```
