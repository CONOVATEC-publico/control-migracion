from gestionData.AbstractDDBB import AbstractDDBB

class Country:
  def __init__(self, rank, pais, puntaje):
    self.rank = rank
    self.pais = pais
    self.puntaje = puntaje

  def getRank(self):
    return self.rank

  def setRank(self, rank):
    self.rank = rank

  def getPais(self):
    return self.pais

  def setPais(self, pais):
    self.pais = pais

  def getPuntaje(self):
    return self.puntaje

  def setPuntaje(self, puntaje):
    self.puntaje = puntaje

#diccionario paises
country_list = [
  Country(1, "Iceland", 1.107),
  Country(2, "New Zeland", 1.269),
  Country(3, "Ireland", 1.288),
  Country(4, "Denmark", 1.296),
  Country(5, "Austria", 1.3),
  Country(6, "Portugal", 1.301),
  Country(7, "Slovenia", 1.316),
  Country(8, "Czech Republic", 1.318),
  Country(9, "Singapore", 1.326),
  Country(10, "Japan", 1.336),
  Country(11, "Switzerland", 1.357),
  Country(12, "Canada", 1.389),
  Country(13, "Hungary", 1.411),
  Country(14, "Finland", 1.439),
  Country(15, "Croatia", 1.44),
  Country(16, "Germany", 1.462),
  Country(17, "Norway", 1.465),
  Country(18, "Malaysia", 1.471),
  Country(19, "Bhutan", 1.481),
  Country(20, "Slovakia", 1.499),
  Country(21, "Netherlands", 1.522),
  Country(22, "Belgium", 1.526),
  Country(23, "Qatar", 1.533),
  Country(24, "Bulgaria", 1.541),
  Country(25, "Poland", 1.552),
  Country(26, "Sweden", 1.564),
  Country(27, "Australia", 1.565),
  Country(28, "Mauritius", 1.57),
  Country(29, "Spain", 1.603),
  Country(30, "Taiwan", 1.618),
  Country(31, "Romania", 1.64),
  Country(32, "Italy", 1.643),
  Country(33, "Estonia", 1.662),
  Country(34, "United Kingdom", 1.667),
  Country(35, "Latvia", 1.673),
  Country(36, "North Macedonia", 1.704),
  Country(37, "Lithuania", 1.724),
  Country(38, "Costa Rica", 1.732),
  Country(39, "Kuwait", 1.739),
  Country(40, "Ghana", 1.759),
  Country(41, "Albania", 1.761),
  Country(42, "Mongolia", 1.775),
  Country(43, "South Korea", 1.779),
  Country(44, "Vietnam", 1.786),
  Country(45, "The Gambia", 1.792),
  Country(46, "Uruguay", 1.795),
  Country(47, "Indonesia", 1.8),
  Country(48, "Botswana", 1.801),
  Country(48, "Montenegro", 1.801),
  Country(50, "Sierra Leone", 1.803),
  Country(51, "Laos", 1.809),
  Country(52, "Serbia", 1.832),
  Country(53, "Greece", 1.838),
  Country(54, "Timor-Leste", 1.839),
  Country(55, "Chile", 1.84),
  Country(56, "Zambia", 1.841),
  Country(57, "Jordan", 1.849),
  Country(58, "Bosnia and Herzegovina", 1.85),
  Country(59, "Equatorial Guinea", 1.863),
  Country(60, "United Arab Emirates", 1.865),
  Country(61, "Panama", 1.876),
  Country(62, "Cambodia", 1.882),
  Country(62, "Moldova", 1.882),
  Country(64, "Oman", 1.889),
  Country(65, "France", 1.895),
  Country(65, "Malawi", 1.895),
  Country(67, "Cyprus", 1.903),
  Country(68, "Namibia", 1.908),
  Country(69, "Argentina", 1.911),
  Country(70, "Senegal", 1.916),
  Country(71, "Kosovo", 1.938),
  Country(72, "Rwanda", 1.945),
  Country(73, "Nepal", 1.947),
  Country(74, "Morocco", 1.969),
  Country(75, "Gabon", 1.973),
  Country(75, "Liberia", 1.973),
  Country(77, "Paraguay", 1.976),
  Country(78, "Angola", 1.982),
  Country(79, "Ecuador", 1.988),
  Country(80, "Bolivia", 1.989),
  Country(81, "Dominican Republic", 1.99),
  Country(81, "Jamaica", 1.99),
  Country(83, "Armenia ", 1.992),
  Country(84, "Madagascar", 1.995),
  Country(85, "Tunisia", 1.996),
  Country(86, "Tanzania", 2.001),
  Country(86, "Uzbekistan", 2.001),
  Country(88, "Trinidad and Tobago", 2.005),
  Country(89, "China", 2.01),
  Country(90, "Sri Lanka", 2.02),
  Country(91, "Kyrgyz Republic ", 2.028),
  Country(92, "Tajikistan", 2.031),
  Country(93, "Eswatini", 2.033),
  Country(94, "Papua New Guinea", 2.046),
  Country(95, "Georgia", 2.065),
  Country(96, "Bangladesh", 2.067),
  Country(97, "Kazakhstan", 2.071),
  Country(98, "Cuba", 2.083),
  Country(99, "Bahrain", 2.085),
  Country(100, "Lesotho", 2.089),
  Country(101, "Peru", 2.091),
  Country(102, "Togo", 2.094),
  Country(103, "Thailand", 2.098),
  Country(104, "Turkmenistan", 2.116),
  Country(105, "Benin", 2.125),
  Country(106, "Guatemala", 2.139),
  Country(107, "Guyana", 2.14),
  Country(108, "Cote d' Ivoire", 2.144),
  Country(109, "Algeria", 2.146),
  Country(110, "Guinea-Bissau", 2.156),
  Country(111, "Republic of the Congo", 2.184),
  Country(112, "Mauritania", 2.193),
  Country(113, "Djibouti", 2.213),
  Country(114, "El Salvador", 2.231),
  Country(115, "Haiti", 2.254),
  Country(116, "Belarus", 2.259),
  Country(117, "Honduras", 2.269),
  Country(118, "South Africa", 2.283),
  Country(119, "Saudi Arabia", 2.288),
  Country(120, "Kenya", 2.303),
  Country(121, "Uganda", 2.309),
  Country(122, "Mozambique", 2.316),
  Country(123, "Guinea", 2.332),
  Country(124, "Nicaragua", 2.334),
  Country(125, "Philippines", 2.339),
  Country(126, "Egypt", 2.342),
  Country(127, "Zimbabwe", 2.35),
  Country(128, "Azerbaijan", 2.437),
  Country(129, "United States of America", 2.44),
  Country(130, "Brazil", 2.465),
  Country(131, "Burundi", 2.47),
  Country(132, "Eritrea", 2.494),
  Country(133, "Palestine", 2.552),
  Country(134, "Israel", 2.576),
  Country(135, "India", 2.578),
  Country(136, "Chad", 2.591),
  Country(137, "Mexico", 2.612),
  Country(138, "Lebanon", 2.615),
  Country(139, "Myanmar", 2.631),
  Country(140, "Niger", 2.655),
  Country(141, "Iran", 2.687),
  Country(142, "Cameroon", 2.709),
  Country(143, "Nigeria", 2.725),
  Country(144, "Colombia", 2.729),
  Country(145, "Turkey", 2.785),
  Country(146, "Burkina Faso", 2.786),
  Country(147, "Pakistan", 2.789),
  Country(148, "Venezuela", 2.798),
  Country(149, "Ethiopia", 2.806),
  Country(150, "Mali", 2.911),
  Country(151, "Libya", 2.93),
  Country(152, "North Korea", 2.942),
  Country(153, "Ukraine", 2.971),
  Country(154, "Sudan", 3.007),
  Country(155, "Central African Republic", 3.021),
  Country(156, "Somalia", 3.125),
  Country(157, "Iraq", 3.157),
  Country(158, "Democratic Republic of the Congo", 3.166),
  Country(159, "South Sudan", 3.184),
  Country(160, "Russia", 3.275),
  Country(161, "Syria", 3.356),
  Country(162, "Yemen", 3.394),
  Country(163, "Afghanistan", 3.554),
]

data = []

for country in country_list:
  coun = [
    country.getRank(),
    country.getPais(),
    country.getPuntaje()
  ]
  data.append(coun)

#pushear toda la data al csv
#AbstractDDBB("country.csv").pushData(data)

#obtener lista
#lista = AbstractDDBB("country.csv").getAll()

#imprimir lista
#for row in lista:
#    print(row)

#obtener objeto por nombre
#print(AbstractDDBB("country.csv").getObject("Afghanistan",1))

#crear nuevo pais
#AbstractDDBB("country.csv").createObject(["164","t","3.54123"])

#actualizar un pais por nombre
#AbstractDDBB("country.csv").updateObject(["164","test","3.54123"], "164", 0)

#borrar un pais por rank
#AbstractDDBB("country.csv").deleteObject("164", 0)