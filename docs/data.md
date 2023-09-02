# Data permanente

Como base de datos se usarán archivos `.csv`. Por defecto, estos archivos serán guardados en la ruta `data/`, sin embargo, puede cambiarse la configuración por medio del método `App.datapath(path)`.

Los archivos `.csv` por defecto para cada tabla son los siguientes:

- `required_person.csv`: Se guardará la lista de personas requisitoriadas (asignadas a la ` class Requisitoriado`)
- `migrant_person.csv`: Se guardará la lista de personas que requirieron el acceso al país por medio de la aplicación y fueron aceptadas (asignadas a la `class Migrant`) #TODO
- `rejected_person.csv`: Se guardará la lista de personas que requirieron el acceso al país por medio de la aplicación y fueron rechazadas (asignadas a la `class Rejected`) #TODO
- `country.csv`: Se guarda la lista de países con sus respectivos índices de paz
