import json

class NeighborDistances:
  def __init__(self):
    self.table = {}

  def add(self, neighbor, port, distance):
    self.table[neighbor] = {
      "port": port,
      "distance": distance
    }

class ForwardingTable:
  def __init__(self):
    self.table = {}
  
  def add(self, dst, neighbor, port, distance):
    self.table[dst] = {
      "neighbor": neighbor,
      "port": port,
      "distance": distance
    }
  
  def toString(self):
    return json.dumps(self.table)
  
  def toTable(table):
    return json.loads(table)