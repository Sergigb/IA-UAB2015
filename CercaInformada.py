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




def RemoveCycles(childrenList):

def RemoveRedundantPaths(childrenList, nodeList, partialCostTable):


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
    """


if __name__ == "__main__":
    main()
