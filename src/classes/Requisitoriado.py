from Persona import Persona
from gestionData.AbstractDDBB import AbstractDDBB
from datetime import datetime

class Requisitoriado(Persona):
    def __init__(
        self,
        nombres,
        apellidos,
        genero,
        fechaNacimiento,
        numeroIdentificacion,
        nacionalidad,
        direccion,
        telefono,
        cargos,
    ):
        super().__init__(
            nombres,
            apellidos,
            genero,
            fechaNacimiento,
            numeroIdentificacion,
            nacionalidad,
            direccion,
            telefono,
        )
        self.cargos = cargos

    def getCargos(self):
        return self.cargos

    def setCargos(self, cargos):
        self.cargos = cargos


requisitoriado_list = [
    Requisitoriado(
        "ROBERTO CARLOS",
        "Gutierrez Garcia",
        "Hombre",
        datetime(1996, 12, 4),
        "00000001",
        "El Salvador",
        "Sin Datos",
        "Sin Datos",
        "Violación en Menor O Incapaz Continuada",
    ),
    Requisitoriado(
        "ROBERTO CARLOS",
        "CHIRI ROMERO",
        "Hombre",
        datetime(1985, 11, 10),
        "00000002",
        "Bolivia",
        "Sin Datos",
        "Sin Datos",
        "Violación",
    ),
    Requisitoriado(
        "ANTONIO JOSE",
        "DE ABREU VIDAL FILHO",
        "Hombre",
        datetime(1994, 1, 3),
        "00000003",
        "Brasil",
        "Sin Datos",
        "Sin Datos",
        "Asesinato, tentativa de asesinato, tortura física y tortura mental.",
    ),
    Requisitoriado(
        "RAFIK KEFI",
        "HANNOUN",
        "Hombre",
        datetime(1989, 5, 16),
        "00000004",
        "Francia",
        "Sin Datos",
        "Sin Datos",
        "INCUMPLIMIENTO DE OBLIGACIÓN",
    ),
    Requisitoriado(
        "MARIUSZ",
        "PRZYSIUDA",
        "Hombre",
        datetime(1971, 4, 2),
        "00000005",
        "Polonia",
        "Sin Datos",
        "Sin Datos",
        "participación en el comercio de cantidades significativas de una sustancia psicotrópica",
    ),
    Requisitoriado(
        "ROSANGELA APARECIDA",
        "RIBEIRO",
        "Mujer",
        datetime(1976, 7, 18),
        "00000006",
        "Brasil",
        "Sin Datos",
        "Sin Datos",
        "Tentativa de asesinato",
    ),
    Requisitoriado(
        "DANIEL PATRICIO",
        "GOROSITO PEREZ",
        "Hombre",
        datetime(1983, 3, 22),
        "00000007",
        "Bolivia",
        "Sin Datos",
        "Sin Datos",
        "ASESINATO",
    ),
    Requisitoriado(
        "RRABIE",
        "RIFFI",
        "Hombre",
        datetime(1986, 2, 10),
        "00000008",
        "Argelia",
        "Sin Datos",
        "Sin Datos",
        "ARRESTAMIENTO, SECUESTRO, DETENCIÓN ABSTRACTA O ARBITRARIA COMETIDOS EN PANDILLA ORGANIZADA",
    ),
    Requisitoriado(
        "EDWIN ALFREDO",
        "ESPINOZA CONDORI",
        "Hombre",
        datetime(1989, 11, 17),
        "00000009",
        "Bolivia",
        "Sin Datos",
        "Sin Datos",
        "VIOLACION - DELITOS SEXUALES",
    ),
    Requisitoriado(
        "TULIO DE JESUS",
        "PINTO GONZALEZ",
        "Hombre",
        datetime(1995, 10, 10),
        "00000010",
        "Guatemala",
        "Sin Datos",
        "Sin Datos",
        "PLAGIO O SECUESTRO Y ASESINATO",
    ),
    Requisitoriado(
        "JOSE DAVID",
        "ZEAS MENDOZA",
        "Hombre",
        datetime(1998, 12, 4),
        "00000011",
        "Nicaragua",
        "Sin Datos",
        "Sin Datos",
        "SECUESTRO EXTORSIVO,ROBO AGRAVADO, TENENCIA ILEGAL DE ARMAS DE FUEGO O MUNICIONES",
    ),
    Requisitoriado(
        "JOSE IVAN",
        "HERNANDEZ CASTRO",
        "Hombre",
        datetime(2001, 5, 25),
        "00000012",
        "Nicaragua",
        "Sin Datos",
        "Sin Datos",
        "SECUESTRO EXTORSIVO, ROBO AGRAVADO, PORTACION ILEGAL DE ARMAS DE FUEGO O MUNICIONES",
    ),
    Requisitoriado(
        "ELSON",
        "DE CARVALHO MELO QUIRINO DE MORAIS",
        "Hombre",
        datetime(1980, 5, 2),
        "00000013",
        "Brasil",
        "Sin Datos",
        "Sin Datos",
        "Trapacero",
    ),
    Requisitoriado(
        "KAPIL",
        "SANGWAN",
        "Hombre",
        datetime(1994, 11, 10),
        "00000014",
        "India",
        "Sin Datos",
        "Sin Datos",
        "ASESINATO, INTENTO DE ASESINATO",
    ),
    Requisitoriado(
        "VIKRAMJEET",
        "SINGH",
        "Hombre",
        datetime(1990, 6, 6),
        "00000015",
        "India",
        "Sin Datos",
        "Sin Datos",
        "Allanamiento de morada para cometer un delito punible con la muerte",
    ),
    Requisitoriado(
        "MISRAEL",
        "CARDONA CABRERA",
        "Hombre",
        datetime(1978, 11, 11),
        "00000016",
        "Guatemala",
        "Sin Datos",
        "Sin Datos",
        "Violación",
    ),
    Requisitoriado(
        "JOSE ARMANDO",
        "ABREGO FUENTES",
        "Hombre",
        datetime(1998, 4, 26),
        "00000017",
        "El Salvador",
        "Sin Datos",
        "Sin Datos",
        "Homicidio Agravado",
    ),
    Requisitoriado(
        "VICTOR MANUEL",
        "CORTEZ LOPEZ",
        "Hombre",
        datetime(1974, 3, 10),
        "00000018",
        "Nicaragua",
        "Sin Datos",
        "Sin Datos",
        "HOMICIDIO",
    ),
    Requisitoriado(
        "MELVIN JOSSUE",
        "ANGEL FLORES",
        "Hombre",
        datetime(1997, 5, 6),
        "00000020",
        "El Salvador",
        "Sin Datos",
        "Sin Datos",
        "Homicidio Agravado.",
    ),
    Requisitoriado(
        "JAIME AMILCAR",
        "GUEVARA PAZ",
        "Hombre",
        datetime(1976, 11, 8),
        "00000021",
        "El Salvador",
        "Sin Datos",
        "Sin Datos",
        "Extorsión Agravada",
    ),
    Requisitoriado(
        "OSCAR ANTONIO",
        "ESCOBAR SÁNCHEZ",
        "Hombre",
        datetime(1985, 12, 2),
        "00000022",
        "El Salvador",
        "Sin Datos",
        "Sin Datos",
        "Organizaciones Terroristas",
    ),
    Requisitoriado(
        "AURELIO",
        "IBARRA MARTINEZ",
        "Hombre",
        datetime(1956, 6, 16),
        "00000023",
        "Bolivia",
        "Sin Datos",
        "Sin Datos",
        "Violación",
    ),
    Requisitoriado(
        "JOSE ABDON",
        "MENDOZA BELTRAN",
        "Hombre",
        datetime(1980, 1, 10),
        "00000024",
        "Bolivia",
        "Sin Datos",
        "Sin Datos",
        "Lesiones con resultado de muerte homicidio o asesinato",
    ),
    Requisitoriado(
        "ABDELKADER",
        "BOUGUETTAIA",
        "Hombre",
        datetime(1987, 6, 29),
        "00000025",
        "Francia",
        "Sin Datos",
        "Sin Datos",
        "PARTICIPACIÓN EN UNA ASOCIACIÓN DE CRIMINALES",
    ),
]

data = []

for requisitoriado in requisitoriado_list:
    req = [
        requisitoriado.getNombres().title(),
        requisitoriado.getApellidos().title(),
        requisitoriado.getGenero(),
        requisitoriado.getFechaNacimiento().strftime("%d/%m/%Y"),
        requisitoriado.getNumeroIdentificacion(),
        requisitoriado.getNacionalidad(),
        requisitoriado.getDireccion(),
        requisitoriado.getTelefono(),
        requisitoriado.getCargos().capitalize()
    ]
    data.append(req)

#pushear toda la data al csv
#AbstractDDBB("required_person.csv").pushData(data)

#crear nuevo requisitoriado
#AbstractDDBB("required_person.csv").createObject(["test nombre","test ap","Hombre", "09/05/2000", "74610635",
#    "Peruano","direc","tel","cargos"
#])
#AbstractDDBB("required_person.csv").deleteObject("74610635",4)

#actualizar lista por documento de identidad
#AbstractDDBB("required_person.csv").updateObject(["test nom","Ap","Hombre", "09/05/2000", "12345678",
#    "Pe","direc","tel","cargos"
#],"12345678",4)

#print(AbstractDDBB("required_person.csv").getObject("12345678",4))

#obtener lista
#lista = AbstractDDBB("required_person.csv").getAll()

#imprimir lista
#for row in lista:
    #print(row)



