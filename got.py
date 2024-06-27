import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import pandas as pd
import streamlit as st
import random
from database import *

def got_func(physics):
  got_net = Network(height="600px", width="100%", font_color="black",heading='Game of Thrones Graph')

# set the physics layout of the network
  got_net.barnes_hut()
  got_data = pd.read_csv("https://github.com/pupimvictor/NetworkOfThrones/blob/master/stormofswords.csv")
  #got_data = pd.read_csv("stormofswords.csv")
  #got_data.rename(index={0: "Source", 1: "Target", 2: "Weight"}) 
  sources = got_data['Source']
  targets = got_data['Target']
  weights = got_data['Weight']

  edge_data = zip(sources, targets, weights)

  for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    got_net.add_node(src, src, title=src)
    got_net.add_node(dst, dst, title=dst)
    got_net.add_edge(src, dst, value=w)

  neighbor_map = got_net.get_adj_list()

# add neighbor data to node hover data
  for node in got_net.nodes:
    node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
    node["value"] = len(neighbor_map[node["id"]])
  if physics:
    got_net.show_buttons(filter_=['physics'])
  got_net.show("gameofthrones.html")
  

def simple_func(physics): 
  nx_graph = nx.cycle_graph(10)
  nx_graph.nodes[1]['title'] = 'Anirban Number 1'
  nx_graph.nodes[1]['group'] = 1
  nx_graph.nodes[3]['title'] = 'I Anirban belong to a different group!'
  nx_graph.nodes[3]['group'] = 10
  nx_graph.add_node(20, size=20, title='couple', group=2)
  nx_graph.add_node(21, size=15, title='couple', group=2)
  nx_graph.add_edge(20, 21, weight=5)
  nx_graph.add_node(25, size=25, label='Anirban lonely', title='Anirban lonely node', group=3)


  nt = Network("500px", "500px",notebook=True,heading='')
  nt.from_nx(nx_graph)
  #physics=st.sidebar.checkbox('add physics interactivity?')
  if physics:
    nt.show_buttons(filter_=['physics'])
  nt.show('Anirban.html')

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r}, {g}, {b})'

def simple_func_nonx(): 
    graph = Network("900px", "1500px",notebook=True,heading='')
    returnVals = graph_dtls_query()
    companies = returnVals.get("Companies")
    for index, row in companies.iterrows():
        print(f"Index: {index}, Name: {row['name']}, Age: {row['sector']}")
        # graph.add_node(index, label=index, color='00ff1e', title="hello")
        graph.add_node(str(row['CompanySeq']), label=row['name'],  title=row['name'],shape='image', image="file://images/company_icon.png")

    sectors = returnVals.get("Sectors")
    for index, row in sectors.iterrows():
        print(f"Index: {index}, Name: {row['sector_name']}")
        graph.add_node(str(row['SectorSeq']), label=row['sector_name'],  color="red" , title=row['sector_name'])

    # managers = returnVals.get("Managers")
    # for index, row in managers.iterrows():
    #     print(f"Index: {index}, Name: {row['name']}")
    #     graph.add_node(str(row['ManagerSeq']), label=row['name'],  color="green" , title=row['name'])

    funds = returnVals.get("Funds")
    for index, row in funds.iterrows():
        # print(f"Index: {index}, Name: {row['name']}")
        graph.add_node(str(row['NewMFSequence']), label=row['fund_name'],  color="yellow" , title=row['fund_name'])


    compSectorRelation = returnVals.get("CompanySectorRelation")
    for index, row in compSectorRelation.iterrows():
         # print(f"Index: {index}, Company: {row['CompanySeq']}")
        graph.add_edge(str(row['CompanySeq']), str(row['SectorSeq']), title="BELONGS")

    # mgrFundRelation = returnVals.get("ManagerFundRelation")
    # for index, row in mgrFundRelation.iterrows():
    #      # print(f"Index: {index}, Company: {row['CompanySeq']}")
    #     graph.add_edge(str(row['NewMFSequence']), str(row['ManagerSeq']), title="MANAGES")
    # graph.add_edge('269371552712097792', '576460752303423488', title="BELONGS")

    fundHoldCompanyRelation = returnVals.get("FundsHoldsCompaniesRelation")
    for index, row in fundHoldCompanyRelation.iterrows():
         # print(f"Index: {index}, Company: {row['CompanySeq']}")
        graph.add_edge(str(row['NewMFSequence']), str(row['CompanySeq']), title="HOLDS")

    
    # # Add 100 nodes
    # NODE_COUNT = 10
    # EDGE_COUNT = 20
    # for i in range(NODE_COUNT):
    #     color = get_random_color()
    #     graph.add_node(i, label="Anirban ID:_node_"+str(i), color=color, title="Anirban label:Person\nprop1:val\nprop2:val2")

    # # Add 300 edges (with some safeguards)
    # edges_added = 0
    # while edges_added < EDGE_COUNT:
    #     # Pick two random nodes to connect
    #     node1 = random.randint(0, NODE_COUNT-1)
    #     node2 = random.randint(0, NODE_COUNT-1)
    #     # Avoid self-loops
    #     if node1 != node2:
    #         graph.add_edge(node1, node2, title="edge_id:8\nlabel:KNOWS\nprop1:val\nprop2:val2")
    #         edges_added += 1

    graph.show('Anirban.html')


def karate_func(physics): 
  G = nx.karate_club_graph()


  nt = Network("500px", "500px",notebook=True,heading='Zachary’s Karate Club graph')
  nt.from_nx(G)
  #physics=st.sidebar.checkbox('add physics interactivity?')
  if physics:
    nt.show_buttons(filter_=['physics'])
  nt.show('karate.html')