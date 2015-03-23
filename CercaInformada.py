#!/usr/bin/python
# -*- coding: latin-1 -*-

# Aquest fitxer conte tot el que es necessari per a la cerca A*:
#   - Definicio de la classe Node, corresponent a la definicio dels nodes de l'arbre
#	- Definicio de la cerca A*
#	- Definicio de les heuristiques a utilitzar.
#   - Eliminar Camins Redundants
#   - Eliminar Cicles
# 
# Autors: Sergi Garcia Bordils, Daniel Sanchez Gil, Adrian Soria Bonilla
# Grup: DX13.01
# _________________________________________________________________________________________
# Intel.ligencia Artificial 
# Grau en Enginyeria Informatica
# Curs 2014 - 2015
# Universitat Autonoma de Barcelona
# _________________________________________________________________________________________

from MapaMetro import *
import math



def RemoveCycles(childrenList):
    nodes = []
    
    for node in childrenList:
        if not node[0] in nodes:
            nodes.append(node[0])
        else:
            return False
        
    return True



def FindClosest(coords,stationList):

    closestStation = None

    for station in stationList:                                  #Busquem l'estació que estigui més aprop de les coordenades de sortida dins de la llista d'estacions
        if(closestStation != None):
            distance_ = math.hypot((coords[0] - station.x),(coords[1] - station.y))
            if(distance_ < distance):                            #Si distància a l'estació actual  és mes petita que l'anterior, substituim l'estació
                closestStation = station
                distance = distance_
        else:                                                    #Quan es fa la primera iteració s'assigna la primera estació de la llista com la més pròxima
            closestStation = station
            distance = math.hypot((coords[0] - station.x),(coords[1] - station.y))

    return closestStation

def DistanceHeuristic(source,destination):
    return math.hypot((destination.x - source.x),(destination.y - source.y))  #Distancia euclidea entre node i destí final
    
def TimeHeuristic(source,destination,estimatedSpeed): 
    time = DistanceHeuristic(source,destination)/estimatedSpeed
    return time

def StationHeuristic(target,destination):
    if target == destination:
        return 0
    elif target.line == destination.line:
        return 1
    else:
        return 2

def TransferHeuristic(source,destination): #Si no estem a la mateixa línea, haurem de fer com a mínim un transbord
    if source.line != destination.line:
        return 1
    else:
        return 0


def AstarAlgorithm(stationList, connections, coord_origin, coord_destination, typePreference, timeTransfers, timeStations):
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
"""
############################################################################################

##                               ________________path_________________
##                              /                                     \
#####Estructura de las listas: [[(ID, coste), (ID, coste), (ID, coste)], [(ID, coste), (ID,coste)]]
##                               \_________/
##                               currentNode


##
##   destinationDic: {ID:coste, ID:coste,...}
##                   \_______/
##                     node

#############################################################################################
##        class Station:
##        # __init__ Constructor of Station Class.
##        def __init__(self, id, name, line, x, y):
##            self.id = id  #station id
##            self.destinationDic = {}  #Dictionary where principal keys refers to the set of stations that it is connected.
##            #The value of this dictionary refers to the time cost between two stations.
##            self.name = name  #station Name
##            self.line = line  # line name string
##            self.x = x  # coordinate X of the station
##            self.y = y  # coordinate Y of the station
##
##
##
##        coord_origin, coord_destination   <---- coordenades
        

    #Busquem l'estació més propera al orígen
    closestStationOrigin = FindClosest(coord_origin,stationList)

    #Busquem l'estació més propera al destí
    closestStationDestination = FindClosest(coord_destination,stationList)
        
    print("L'estacio mes proxima al origen es ", closestStationOrigin.name)
    print("L'estacio mes proxima al desti es ", closestStationDestination.name)
    typePreference = int(typePreference)


##    if typePreference == 2:
    setNextStations(stationList, timeStations)    #matriu de costos en temps
##    else:
##        setNextStations (stationList, connections)    #la resta de casos usen la matriu d'adjacència

    List = [[(closestStationOrigin.id, 0)]]      #El primer element de la llista de camins és el primer node
    currentNode = (None, None)
    num_expanded_nodes = 0
    visitedNodes =[]

    

    while List and currentNode[0] != closestStationDestination.id:          #Mentres la llista no estigui buida o el primer node del primer camí(path) no sigui el destí, seguim expandint
        num_expanded_nodes = num_expanded_nodes + 1
        path = List.pop(0)                                                  ##### "path" es la llista on estan les tuples amb les IDs i els costos
        currentNode = path[0]                                               ### ID del node on estem ara
        destinationDic = stationList[currentNode[0]-1].destinationDic       #copiem el diccionari de nodes adjacents al node actual (ID y cost) (es troba a la llista d'estacions)

        for node in destinationDic:                                         #Explorem tots els nodes adjacents que es troben en el diccionari

            nextStation = stationList[node-1]                               #Assignem a nextStation i currentStation les estacions corresponents (de la llista stationList) al node que estem 
            currentStation = stationList[currentNode[0]-1]                  #expandint i el node actual, així podrem obtenir les distàncies entre l'un i l'altre

            if currentStation.id not in visitedNodes:                       #Recollim els nodes visitats per l'output de la funció
                visitedNodes.append(currentStation.id)


            if typePreference == 0:
                partialCost = math.hypot((nextStation.x - currentStation.x),(nextStation.y - currentStation.y))
                h = DistanceHeuristic(nextStation,closestStationDestination)
                partialCost = partialCost + h
    
            elif typePreference == 1:
                partialCost = 1
                h = StationHeuristic(nextStation,closestStationDestination)
                partialCost = partialCost + h
                
            elif typePreference == 2:
                partialCost = timeStations[currentStation.id][nextStation.id]
                estimatedSpeed = (math.hypot((nextStation.x - currentStation.x),(nextStation.y - currentStation.y)))/partialCost #V=x/t: assumim que la velocitat serà constant

                if currentStation.line != nextStation.line:
                    partialCost = partialCost + timeTransfers[currentStation.id][nextStation.id]
                    
                h = TimeHeuristic(nextStation,closestStationDestination,estimatedSpeed)
                partialCost = partialCost + h
                
            elif typePreference == 3:
                if currentStation.line != nextStation.line:
                    partialCost = 1
                else:
                    partialCost = 0
                h = TransferHeuristic(nextStation,closestStationDestination)
                partialCost = partialCost + h
                
            else:
                raise AttributeError
            
            
            cost = partialCost + currentNode[1]                             #Creem una nova tupla amb el cost i la ID del node adjacent que estem expandint
            ID = node
            tempNode = (ID, cost)
            tempPath = list(path)                                           #Copiem el camí actual (el path) i inserim la tupla amb la ID i el cost 
            tempPath.insert(0, tempNode)
            
            n = RemoveCycles(tempPath)                                      #Aquesta funció buscará si el node que hem expandit ja l'havíem visitat anteriorment en aquest camí. Si es la primera
                                                                            #vegada que el visitem, l'afegim a la llista de camins (List)
            if n:
                pos = 0
                for listPath in List:                                       #Inserim de forma ordenada el nou camí en la llista, d'aquesta forma la llista queda ordenada de menor cost a major
                    firstNode = listPath[0]
                    if firstNode[1] < cost:
                        pos = pos + 1
            
                List.insert(pos, tempPath)
            

        #print List
        if currentNode[0] == closestStationDestination.id:                  #Si el primer node del primer camí és el destí, l'imprimim (i després la funció acabará)

            i = 0

            for item in path:                                               #Elimina les estacions del principi de la ruta que estiguin repetides
                nextItem = path[i+1]
                station = stationList[item[0]-1]
                station_ = stationList[nextItem[0]-1]
                if station.name == station_.name:
                    path.pop(i)
                else:
                    break
                i+=1

            i = len(path) - 1                                               #Elimina les estacions del final de la ruta que estiguin repetides
            for item in reversed(path):
                nextItem = path[i-1]
                station = stationList[item[0]-1]
                station_ = stationList[nextItem[0]-1]
                if station.name == station_.name:
                    path.pop(i)
                else:
                    break
                i-=1


            distance = 0
            time = 0
            transfers = 0
            walk = reversed(path)
            stopStations = len(path)-1
            depth = len(path)
            min_distance_origin = math.hypot((coord_origin[0] - closestStationOrigin.x),(coord_origin[1] - closestStationOrigin.y))
            min_distance_destination = math.hypot((coord_destination[0] - closestStationDestination.x),(coord_destination[1] - closestStationDestination.y))

            prev = None
            
            for node in reversed(path):
                station = stationList[node[0]-1]
                print station.id
                if prev != None:
                    print station, prev, station.id, prev.id
                    partialDist = math.hypot((prev.x - station.x),(prev.y - station.y))
                    distance = distance + partialDist
                    partialTime = timeStations[prev.id][station.id]
                    if prev.line != station.line:
                        partialTime = partialTime + timeTransfers[prev.id][station.id]
                        transfers = transfers + 1
                prev = station
            print time,distance,transfers,stopStations,num_expanded_nodes,depth,visitedNodes,min_distance_origin,min_distance_destination
            
            return (time,distance,transfers,stopStations,num_expanded_nodes,depth,visitedNodes,min_distance_origin,min_distance_destination)
            
                        

############################################################################################

if __name__ == "__main__":
    main()



def test(coord_origin, coord_destination, typePreference):    #coord_origin i coord_destination s'han de cridar com una tupla com per exempe: (coord_destination_x, coord_destination_y)

    stationList = readStationInformation("Stations.txt")      #Llista d'estacions
    matAdjacencia = readCostTable("Connections.txt")          #Matriu d'adjacència de les estacions 
    timeStations = readCostTable("TempsEstacions.txt")        #Matriu de costos entre estacions
    timeTransfers = readCostTable("TempsTransbordaments.txt") #Matriu de costos de transbord
    t = AstarAlgorithm(stationList, matAdjacencia, coord_origin, coord_destination, typePreference, timeTransfers, timeStations)
    return t
