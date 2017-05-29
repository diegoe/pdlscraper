pdlscraper: A web scraper for proyectosdeley.pe
====

pdlscraper analiza la información publicada por el Congreso de la República y la indexa para poder mostrarla en http://proyectosdeley.pe.

proyectosdeley.pe es un proyecto de la ONG Hiperderecho y la asociación Contribuyentes por Respeto.
El código de la aplicación web y este scraper han sido desarrollados por [Carlos Peña](https://github.com/carlosp420).

## Tareas recurrentes

Es necesario instalar algunas tareas en crontab (o lo que se prefiera)
para asegurar que el scraper se ejecute.

```shell
52 20 * * * scrapy crawl pdfurl >> scraping_pdf_url_log.txt             2>&1
0 */6 * * * scrapy crawl proyecto >> scraping_proyecto.log.txt          2>&1
0 3 * * 2   scrapy crawl seguimientos >> scraping_seguimientos.log.txt  2>&1
0 3 * * 3   scrapy crawl iniciativa >> scraping_iniciativas.log.txt     2>&1
0 3 * * 4   scrapy crawl updater >> scraping_updater.log.txt            2>&1
0 3 * * 5   scrapy crawl expediente >> scraping_expediente.log.txt      2>&1

0 6 * * *   proyectos_de_ley/manage.py update_index --age=24 --settings=proyectos_de_ley.settings.production >> updating_index.log.txt 2>&1
```

La última tarea (manage.py) es necesaria para que django esté al tanto de los cambios en la base de datos.

## Configuración de base de datos

pdlscraper guarda los datos analizados e indexados en la base de datos de proyectosdeley.pe. Es necesario tener una instalación de proyectosdeley.pe para poder usar pdlscraper.

pdlscraper lee un archivo 'config.json' en el root del repositorio que sigue la siguiente configuración:

```json
{
    "drivername": "postgresql",

    "username": "username",
    "password": "password",
    "host": "localhost",
    "port": "5432",
    "database": "pdl",

    "crawlera_enabled": "false",
    "crawlera_user": "optional",
    "crawlera_pass": "optional",
    "legislature": "2016"
}
```
La configuración y uso de crawlera para acelerar el scraping es opcional.
