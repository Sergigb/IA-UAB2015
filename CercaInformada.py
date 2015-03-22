# Aquest fitxer conte tot el que es necessari per a la cerca A*:
#   - Definicio de la classe Node, corresponent a la definicio dels nodes de l'arbre
#	- Definicio de la cerca A*
#	- Definicio de les heuristiques a utilitzar.
#   - Eliminar Camins Redundants
#   - Eliminar Cicles
# 
# Autors: 
# Grup: 
# _________________________________________________________________________________________
# Intel.ligencia Artificial 
# Grau en Enginyeria Informatica
# Curs 2014 - 2015
# Universitat Autonoma de Barcelona
# _________________________________________________________________________________________

from MapaMetro import *
import math




def RemoveCycles(childrenList):
    pass

def RemoveRedundantPaths(childrenList, nodeList, partialCostTable):
    pass


def AstarAlgorithm(stationList, connections, coord_origin, coord_destination, typePreference, timeTransfers,
                   timeStations):
    """
     AstarAlgorithm: main function. It is the connection between the GUI and the AStar search code.
     INPUTS:
            - stationList: LIST of the stations of a city. (- id, name, destinationDic, line, x, y -)
            - connections: DICTIONARY set of possible connections between the stations (REAL connections)
            - coord_origin: TUPLE of two values referring to the origin coordinates
            - coord_destination: TUPLE of two values referring to the destination coordinates
            - typePreference: INTEGER Value to indicate the preference selected: 0 - minimum Distance | 1- minimum Stops | 2- minimum Time | 3 - minimum transfers
            - timeTransfers: DICTIONARY time of transfers between two different lines in a certain station
            - timeStations: DICTIONARY  time that takes the train to go from a station to the other (in the same line)
    OUTPUTS:
            - time: REAL total required time to make the route
            - distance: REAL total distance made in the route
            - transfers: INTEGER total transfers made in the route
            - stopStations: INTEGER total stops made in the route
            - num_expanded_nodes: INTEGER total expanded nodes to get the optimal path
            - depth: INTEGER depth of the solution
            - visitedNodes: LIST of INTEGERS, ID's of the visited nodes
            - min_distance_origin: REAL the distance of the origin_coordinates to the closest station
            - min_distance_destination: REAL the distance of the destination_coordinates to the closest station

            optimalPath.time, optimalPath.walk, optimalPath.transfers, optimalPath.num_stopStation, len(
        expandedList), len(optimalPath.parentsID), visitedNodes, idsOptimalPath, min_distance_origin, min_distance_destination


        class Station:
    # __init__ Constructor of Station Class.
    def __init__(self, id, name, line, x, y):
        self.id = id  #station id
        self.destinationDic = {}  #Dictionary where principal keys refers to the set of stations that it is connected.
        #The value of this dictionary refers to the time cost between two stations.
        self.name = name  #station Name
        self.line = line  # line name string
        self.x = x  # coordinate X of the station
        self.y = y  # coordinate Y of the station



coord_origin, coord_destination   <---- coordenades
        
    """
    #Busquem l'estació més propera al orígen
    closestStationOrigin = None

    for station in stationList:
        
        if(closestStationOrigin != None):
            distance_ = math.sqrt( (coord_origin[0] - station.x)**2 + (coord_origin[1] - station.y)**2 )
            if(distance_ < distance):
                closestStationOrigin = station
                distance = distance_
        else:
            closestStationOrigin = station
            distance = math.sqrt( (coord_destination[0] - station.x)**2 + (coord_destination[1] - station.y)**2 )

    closestStationDestination = None
        
    for station in stationList:
        
        if(closestStationDestination != None):
            distance_ = math.sqrt( (coord_destination[0] - station.x)**2 + (coord_destination[1] - station.y)**2 )
            if(distance_ < distance):
                closestStationDestination = station
                distance = distance_
        else:
            closestStationDestination = station
            distance = math.sqrt( (coord_destination[0] - station.x)**2 + (coord_destination[1] - station.y)**2 )
        
    print("L'estacio mes proxima al origen es ", closestStationOrigin.name)
    print("L'estacio mes proxima al desti es ", closestStationDestination.name)
    










    


#if __name__ == "__main__":
#    main()



def test(coord_origin, coord_destination, typePreference):    #coord_origin i coord_destination s'han de cridar com una tupla com per exempe: (coord_destination_x, coord_destination_y)

    stationList = readStationInformation("Stations.txt")      #Llista d'estacions
    matAdjacencia = readCostTable("Connections.txt")          #Matriu d'adjacència de les estacions 
    timeStations = readCostTable("TempsEstacions.txt")        #Matriu de costos entre estacions
    timeTransfers = readCostTable("TempsTransbordaments.txt") #Matriu de costos de transbord
    AstarAlgorithm(stationList, matAdjacencia, coord_origin, coord_destination, typePreference, timeTransfers, timeStations)
    
    

















