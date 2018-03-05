#!/usr/bin/env python

"""
Original Code: https://gist.github.com/millionsmile/3682029

Drawing and Coloring Code: https://networkx.github.io/documentation/networkx-1.9/examples/drawing/labels_and_colors.html

Labeling Code: https://gawron.sdsu.edu/python_for_ss/course_core/book_draft/Social_Networks/Networkx.html
"""

import networkx as NX
import networkx.algorithms.centrality as NC
import pylab as P

# Removes an edge from the Karate Club graph with the highest edge betweenness
def updateGraph(G):
    ebc = NC.edge_betweenness(G)
    maxs = 0
    medge = None
    for k, v in ebc.items():
        if maxs < v:
            medge, maxs = k, v
    G.remove_edge(*medge)
    #return G

# Draws the current state of the Karate Club graph
def drawGraph(G, pos, output):
    
    # Draws the two factions of nodes, denoted by different colors (Mr. Hi: John A: )
    NX.draw_networkx_nodes(G,pos,nodelist=[0,1,3,4,5,6,7,10,11,12,13,16,17,19,21],node_color='r',node_size=500,alpha=0.8)
    NX.draw_networkx_nodes(G,pos,nodelist=[2,8,9,14,15,18,20,22,23,24,25,26,27,28,29,30,31,32,33],node_color='g',node_size=500,alpha=0.8)

    # Draws the edges between the corresponding nodes
    NX.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
    
    # Draws the labels for each node (e.g., 1, 2, 3, ... n)
    new_labels = dict((x,x + 1) for x in G.nodes())
    NX.draw_networkx_labels(G,pos,new_labels,font_size=14,font_color='black')
    
    # Turns the axis off, and saves the graph to the corresponding 'output' file
    P.axis("off")
    P.savefig(output)
    P.draw()
    P.close()

# Function that iteratively removes an edge from the original graph, and saves the new graph to a .png file
# Note: This function loops until all edges have been removed! 
G=NX.karate_club_graph()
eNum = G.number_of_edges()
for i in range(eNum):
    pos = NX.spring_layout(G)
    output = "img/karate%(id)02d.png" % {"id": i}
    drawGraph(G, pos, output)
    updateGraph(G)
