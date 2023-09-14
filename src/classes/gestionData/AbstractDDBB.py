import csv
import os 

class AbstractDDBB:
  def __init__(self,filename):
    #self.datapath = datapath
    self.filename = filename
    # self.dataObject = dataObject

  def getObject(self,id, index):
    data = self.getAll()
    for row in data:
      if row[index] == id:
        return row

  def getAll(self):
    data = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(script_dir, '../../../data/' + self.filename)

    with open(ruta_csv,"r",encoding='utf-8') as f:
      reader = csv.reader(f,delimiter=";")
      for row in reader:
        data.append(row)

    return data

  def pushData(self,list):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(script_dir, '../../../data/' + self.filename)    

    with open(ruta_csv,"w",newline="",encoding="utf-8") as file:
      writer = csv.writer(file, delimiter=";")
      writer.writerows(list)

  def createObject(self,obj):
    data = self.getAll()
    data.append(obj)
    self.pushData(data)

  def deleteObject(self, id,index):
    data = self.getAll()
    auxList = []
    for row in data:
      if row[index] !=  id:
        auxList.append(row)
    
    self.pushData(auxList)

  def updateObject(self,obj,id,index):
    data = self.getAll()
    auxList = []
    for row in data:
      if row[index] !=  id:
        auxList.append(row)
      else:
        auxList.append(obj)
    self.pushData(auxList)
