

#%%

# Importing necessary modules: NetworkX to generate DAG, MatPlotLib to view DAG
import networkx as nx
from networkx.drawing import nx_pydot
from networkx.drawing.nx_pydot import write_dot
import matplotlib.pyplot as plt
import graphviz as gv
from graphviz import render


# Initiating the DiGraph and assigning it to the variable G
G = nx.DiGraph()


# SQL used to generate data for Relationship CSV File
    # SELECT IA.InvestorID, IA.InvestmentID, IA.OwnershipPct
    # FROM BKUSLP.HARMONY_TEST.DBO.IA_RELATIONSHIP IA, BKUSLP.HARMONY_TEST.DBO.ENTITY EN
    # WHERE IA.InvestorID = EN.ENTITYID AND EN.LEDGCODE <> 'CA'



# Adding nodes to my DiGraph, however, this isn't necessary for DiGraphs.  I can simply add the edges and NetworkX will create the nodes for me.
G.add_nodes_from(['F0000PT1', 'F0355G00', 'P0206B01', 'P0226B01', 'P0226B02', 'F000E', 'P0122E00', 'P0130E00', 'P0154E00', 'P0156E00', 'P0180E00', 'P0189E00', 'P0184E00', 'P0225B01', 'P0225E00', 'P0230B01', 'P0230B02', 'P0230E00', 'P0231B01', 'P0231E00', 'P0265E00', 'F0355E00', 'F0501', 'P0248J01', 'P0248E00', 'P0111E00', 'F0355LP', 'P0184B01', 'P0265B01', 'P0189B02', 'F000R', 'P0236E01', 'P0236E00', 'P0254E00', 'P0248B01', 'P0122B01', 'P0122B02', 'P0122B03', 'P0130B01', 'P0154B01', 'P0156B01', 'P0180B01', 'P0189B01', 'P0111B01', 'P0111B02', 'P0111B03', 'F0355RT', 'F000LP', 'F000EG', 'P0236B01', 'P0236B02', 'P0254B01', 'P0254B02', 'P0345E00', 'F0279E00', 'P0348E01', 'F000RGC', 'F00YTC', 'P0038E00', 'P0288E00', 'P0330E00', 'P0347E00', 'F0279G00', 'P0369E00', 'P0370E00', 'P0355E00', 'F0318E00', 'F0318G00', 'P0093E00', 'P0131E00', 'P0136E00', 'P0137E00', 'P0139E00', 'P0145E00', 'P0146E00', 'P0151E00', 'P0162E00', 'P0165E00', 'P0172E00', 'P0175E00', 'P0177E00', 'P0186E00', 'P0193E00', 'P0196E00', 'P0202E00', 'P0233E00', 'P0243E00', 'P0252E00', 'P0253E00', 'P0261E00', 'P0262E00', 'P0269E00', 'P0278E00', 'P0280E00', 'P0281E00', 'P0286E00', 'P0291E00', 'P0292E00', 'P0293E00', 'P0297E00', 'P0298E00', 'P0300E00', 'P0301E00', 'P0302E00', 'P0302RT', 'P0305E00', 'P0307E00', 'P0310E00', 'P0312E00', 'P0313E00', 'P0314E00', 'P0315E00', 'P0316E00', 'P0317E00', 'P0320E00', 'P0321E00', 'P0325E00', 'P0326E00', 'P0327E00', 'P0328E00', 'P0329E00', 'P0332E00', 'P0333E00', 'P0335E00', 'P0335RT', 'P0341E00', 'P0344E00', 'P0346E00', 'P0348E00', 'P0354E00', 'P0354J01', 'P0356E00', 'P0358E00', 'P0360E00', 'P0361E00', 'P0362E00', 'P0363E00', 'P0364E00', 'P0365E00', 'P0366E00', 'P0367E00', 'P0368E00', 'F000J', 'F000LT', 'F000M', 'F000NT', 'F000T', 'F0331E00', 'F0331G00', 'F0370G00', 'P0249E00', 'P0372E00', 'P0357E00', 'P0322G00', 'P0322E00', 'P0294E00', 'P0373E00', 'P0371E00', 'P0269E01', 'P0354D01', 'P0356B01', 'P0356B02', 'P0358J01', 'P0360J01', 'P0361B01', 'P0361B02', 'P0362J01', 'P0363B01', 'P0363B02', 'P0364B01', 'P0365B01', 'P0366B01', 'P0367B01', 'P0367B02', 'P0368B01', 'P0368B02', 'P0368B03', 'P0370B01', 'P0281B01', 'P0286B01', 'P0286B02', 'P0291B01', 'P0291B02', 'P0293B01', 'P0297B01', 'P0298B01', 'P0298B02', 'P0300B01', 'P0301B01', 'P0302B01', 'P0302B02', 'P0305B01', 'P0307B01', 'P0310B01', 'P0312B01', 'P0313B01', 'P0314B01', 'P0314B02', 'P0315B01', 'P0316B01', 'P0317B01', 'P0320J01', 'P0269J02', 'P0269J01', 'F0331LP', 'P0348J01', 'P0333J01', 'P0323E00', 'P0336E00', 'P0337E00', 'P0338E00', 'P0340E00', 'P0342E00', 'P0343E00', 'P0349E00', 'P0350E00', 'P0351E00', 'P0352E00', 'P0353E00', 'P0359E00', 'F0318LP', 'F0318RT', 'P0093B01', 'P0131B01', 'P0131B02', 'P0131B03', 'P0131B04', 'P0131B05', 'P0131B06', 'P0355B03', 'P0355B01', 'P0355B02', 'P0186B01', 'P0186B02', 'P0186B03', 'P0186B04', 'P0193B01', 'P0196B01', 'P0202B01', 'P0233J01', 'P0243B01', 'P0243B02', 'P0243B03', 'P0249J01', 'P0252B01', 'P0252B02', 'P0335B01', 'P0341B01', 'P0344B01', 'P0344B02', 'P0345B01', 'P0346B01', 'P0136B01', 'P0137B01', 'P0137B02', 'P0139B01', 'P0139B02', 'P0139B03', 'P0139B04', 'P0139B05', 'P0145B01', 'P0146B01', 'P0146B02', 'P0146B03', 'P0146B04', 'P0146B05', 'P0146B06', 'P0151B01', 'P0151B02', 'P0151B03', 'P0162B01', 'P0165B01', 'P0165B02', 'P0175B01', 'P0175B02', 'P0175B03', 'P0175B04', 'P0175B05', 'P0177J01', 'P0354B01', 'P0354B02', 'P0354B03', 'P0354B04', 'P0354B05', 'P0354B06', 'P0252B03', 'P0252B04', 'P0253B01', 'P0253B02', 'P0253B03', 'P0253B04', 'P0253B05', 'P0253B06', 'P0253B07', 'P0253B08', 'P0253B09', 'P0253B10', 'P0261B01', 'P0262B01', 'P0278J01', 'P0280B01', 'P0280B02', 'P0200E00', 'P0321B01', 'P0325B01', 'P0325B02', 'P0326B01', 'P0327B01', 'P0328B01', 'P0329B01', 'P0329B02', 'P0338J01', 'F0279LP', 'F0279RT', 'F0331RT', 'P0372B01', 'P0372B02', 'P0372B03', 'P0322J01', 'P0093B02', 'P0129E00', 'P0164E00', 'P0172J01', 'P0269B99', 'P0329B99', 'P0341B02', 'P0345B02', 'P0294B01', 'P0373B01', 'P0373B02', 'P0313B02', 'P0243B99', 'P0207E00', 'P0342B01', 'P0358J02', 'P0358RT', 'P0359B01', 'P0360B01', 'P0360B02', 'P0360D01', 'P0362D01', 'P0320J02', 'P0320J03', 'P0164B01', 'P0269B01', 'P0269B02', 'P0279J01', 'P0339J01', 'P0338B01', 'P0339B01', 'P0348D01', 'P0348D02', 'P0348D03', 'P0336J01', 'P0318J01', 'P0233J02', 'P0249B01', 'P0333B01', 'P0333B02', 'P0333B03', 'P0337J01', 'P0340J01', 'P0343B01', 'P0343B02', 'P0343B03', 'P0349B01', 'P0177J02', 'P0350B01', 'P0351B01', 'P0352B01', 'P0352B02', 'P0353B01', 'P0278B01', 'P0323B01', 'P0323B02', 'P0331J01', 'P0322B01', 'P0129B01', 'P0129B02', 'P0172B01', 'P0269J03', 'P0172B02', 'P0207B01', 'P0200B01', 'P0200B02', 'P0358J03', 'P0318B01', 'P0331B01', 'P0331B02', 'P0279B01', 'P0279B02', 'P0279B99', 'P0233B01', 'P0233B02', 'P0336B01', 'P0337B01', 'P0340B01', 'P0177B01', 'P0177B02', 'P0320B01', 'P0320B02', 'P0320B03', 'P0269B03', 'P0358B01', 'P0358D01'])

# Adding edges to my DiGraph to connect my nodes.
G.add_edges_from([('F0000PT1', 'F0000'), ('F0000', 'F0355G00'), ('F0000', 'P0206B01'), ('F0000', 'P0226B01'), ('F0000', 'P0226B02'), ('F0000', 'F000E'), ('F0000', 'P0122E00'), ('F0000', 'P0130E00'), ('F0000', 'P0154E00'), ('F0000', 'P0156E00'), ('F0000', 'P0180E00'), ('F0000', 'P0189E00'), ('F0000', 'P0184E00'), ('F0000', 'P0225B01'), ('F0000', 'P0225E00'), ('F0000', 'P0230B01'), ('F0000', 'P0230B02'), ('F0000', 'P0230E00'), ('F0000', 'P0231B01'), ('F0000', 'P0231E00'), ('F0000', 'P0265E00'), ('F0000', 'F0355E00'), ('F0000', 'F0501'), ('F0000', 'P0248J01'), ('F0000', 'P0248E00'), ('F0000', 'P0111E00'), ('F0355E00', 'F0355LP'), ('F0355G00', 'F0355LP'), ('P0184E00', 'P0184B01'), ('P0265E00', 'P0265B01'), ('P0189E00', 'P0189B02'), ('F000E', 'F000R'), ('F0501', 'P0236E01'), ('F0501', 'P0236E00'), ('F0501', 'P0254E00'), ('P0248J01', 'P0248B01'), ('P0122E00', 'P0122B01'), ('P0122E00', 'P0122B02'), ('P0122E00', 'P0122B03'), ('P0130E00', 'P0130B01'), ('P0154E00', 'P0154B01'), ('P0156E00', 'P0156B01'), ('P0180E00', 'P0180B01'), ('P0189E00', 'P0189B01'), ('P0225E00', 'P0225B01'), ('P0230E00', 'P0230B01'), ('P0230E00', 'P0230B02'), ('P0231E00', 'P0231B01'), ('P0111E00', 'P0111B01'), ('P0111E00', 'P0111B02'), ('P0111E00', 'P0111B03'), ('P0248E00', 'P0248J01'), ('F0355LP', 'F0355RT'), ('F000R', 'F000LP'), ('F000R', 'F000EG'), ('P0236E01', 'P0236E00'), ('P0236E00', 'P0236B01'), ('P0236E00', 'P0236B02'), ('P0254E00', 'P0254B01'), ('P0254E00', 'P0254B02'), ('F000LP', 'P0345E00'), ('F000LP', 'F0279E00'), ('F000LP', 'P0348E01'), ('F000EG', 'F000LP'), ('F000LP', 'F000RGC'), ('F000LP', 'F00YTC'), ('F000LP', 'P0038E00'), ('F000LP', 'P0288E00'), ('F000LP', 'P0330E00'), ('F000LP', 'P0347E00'), ('F000LP', 'F0279G00'), ('F000LP', 'P0369E00'), ('F000LP', 'P0370E00'), ('F0355RT', 'P0355E00'), ('F000LP', 'F0318E00'), ('F000LP', 'F0318G00'), ('F000LP', 'P0093E00'), ('F000LP', 'P0131E00'), ('F000LP', 'P0136E00'), ('F000LP', 'P0137E00'), ('F000LP', 'P0139E00'), ('F000LP', 'P0145E00'), ('F000LP', 'P0146E00'), ('F000LP', 'P0151E00'), ('F000LP', 'P0162E00'), ('F000LP', 'P0165E00'), ('F000LP', 'P0172E00'), ('F000LP', 'P0175E00'), ('F000LP', 'P0177E00'), ('F000LP', 'P0186E00'), ('F000LP', 'P0193E00'), ('F000LP', 'P0196E00'), ('F000LP', 'P0202E00'), ('F000LP', 'P0233E00'), ('F000LP', 'P0243E00'), ('F000LP', 'P0252E00'), ('F000LP', 'P0253E00'), ('F000LP', 'P0261E00'), ('F000LP', 'P0262E00'), ('F000LP', 'P0269E00'), ('F000LP', 'P0278E00'), ('F000LP', 'P0280E00'), ('F000LP', 'P0281E00'), ('F000LP', 'P0286E00'), ('F000LP', 'P0291E00'), ('F000LP', 'P0292E00'), ('F000LP', 'P0293E00'), ('F000LP', 'P0297E00'), ('F000LP', 'P0298E00'), ('F000LP', 'P0300E00'), ('F000LP', 'P0301E00'), ('F000LP', 'P0302E00'), ('F000LP', 'P0302RT'), ('F000LP', 'P0305E00'), ('F000LP', 'P0307E00'), ('F000LP', 'P0310E00'), ('F000LP', 'P0312E00'), ('F000LP', 'P0313E00'), ('F000LP', 'P0314E00'), ('F000LP', 'P0315E00'), ('F000LP', 'P0316E00'), ('F000LP', 'P0317E00'), ('F000LP', 'P0320E00'), ('F000LP', 'P0321E00'), ('F000LP', 'P0325E00'), ('F000LP', 'P0326E00'), ('F000LP', 'P0327E00'), ('F000LP', 'P0328E00'), ('F000LP', 'P0329E00'), ('F000LP', 'P0332E00'), ('F000LP', 'P0333E00'), ('F000LP', 'P0335E00'), ('F000LP', 'P0335RT'), ('F000LP', 'P0341E00'), ('F000LP', 'P0344E00'), ('F000LP', 'P0346E00'), ('F000LP', 'P0348E00'), ('F000LP', 'P0354E00'), ('F000LP', 'P0354J01'), ('F000LP', 'P0356E00'), ('F000LP', 'P0358E00'), ('F000LP', 'P0360E00'), ('F000LP', 'P0361E00'), ('F000LP', 'P0362E00'), ('F000LP', 'P0363E00'), ('F000LP', 'P0364E00'), ('F000LP', 'P0365E00'), ('F000LP', 'P0366E00'), ('F000LP', 'P0367E00'), ('F000LP', 'P0368E00'), ('F000LP', 'F000J'), ('F000LP', 'F000LT'), ('F000LP', 'F000M'), ('F000LP', 'F000NT'), ('F000LP', 'F000T'), ('F000LP', 'F0331E00'), ('F000LP', 'F0331G00'), ('F000LP', 'F0370G00'), ('F000LP', 'P0249E00'), ('F000LP', 'P0372E00'), ('F000LP', 'P0357E00'), ('F000LP', 'P0322G00'), ('F000LP', 'P0322E00'), ('F000LP', 'P0294E00'), ('F000LP', 'P0373E00'), ('F000LP', 'P0371E00'), ('F000LP', 'P0269E01'), ('P0354J01', 'P0354D01'), ('P0356E00', 'P0356B01'), ('P0356E00', 'P0356B02'), ('P0358E00', 'P0358J01'), ('P0360E00', 'P0360J01'), ('P0361E00', 'P0361B01'), ('P0361E00', 'P0361B02'), ('P0362E00', 'P0362J01'), ('P0363E00', 'P0363B01'), ('P0363E00', 'P0363B02'), ('P0364E00', 'P0364B01'), ('P0365E00', 'P0365B01'), ('P0366E00', 'P0366B01'), ('P0367E00', 'P0367B01'), ('P0367E00', 'P0367B02'), ('P0368E00', 'P0368B01'), ('P0368E00', 'P0368B02'), ('P0368E00', 'P0368B03'), ('P0370E00', 'P0370B01'), ('P0281E00', 'P0281B01'), ('P0286E00', 'P0286B01'), ('P0286E00', 'P0286B02'), ('P0291E00', 'P0291B01'), ('P0291E00', 'P0291B02'), ('P0293E00', 'P0293B01'), ('P0297E00', 'P0297B01'), ('P0298E00', 'P0298B01'), ('P0298E00', 'P0298B02'), ('P0300E00', 'P0300B01'), ('P0301E00', 'P0301B01'), ('P0302E00', 'P0302RT'), ('P0302RT', 'P0302B01'), ('P0302RT', 'P0302B02'), ('P0305E00', 'P0305B01'), ('P0307E00', 'P0307B01'), ('P0310E00', 'P0310B01'), ('P0312E00', 'P0312B01'), ('P0313E00', 'P0313B01'), ('P0314E00', 'P0314B01'), ('P0314E00', 'P0314B02'), ('P0315E00', 'P0315B01'), ('P0316E00', 'P0316B01'), ('P0317E00', 'P0317B01'), ('P0320E00', 'P0320J01'), ('F0370G00', 'P0370E00'), ('P0269E00', 'P0269J02'), ('P0269E00', 'P0269J01'), ('F000NT', 'F0279E00'), ('P0348E01', 'P0348E00'), ('F0331E00', 'F0318E00'), ('F0331E00', 'F0331LP'), ('P0348E00', 'P0348J01'), ('F000LT', 'P0333J01'), ('F000M', 'F000T'), ('F000M', 'P0249E00'), ('F000M', 'P0323E00'), ('F000M', 'P0336E00'), ('F000M', 'P0337E00'), ('F000M', 'P0338E00'), ('F000M', 'P0340E00'), ('F000M', 'P0342E00'), ('F000M', 'P0343E00'), ('F000M', 'P0349E00'), ('F000M', 'P0350E00'), ('F000M', 'P0351E00'), ('F000M', 'P0352E00'), ('F000M', 'P0353E00'), ('F000M', 'P0359E00'), ('F000NT', 'F0318E00'), ('F000NT', 'P0348E00'), ('F000T', 'F0318LP'), ('F0318E00', 'F0318LP'), ('F0318E00', 'F0318RT'), ('F0318G00', 'F0318LP'), ('P0093E00', 'P0093B01'), ('P0131E00', 'P0131B01'), ('P0131E00', 'P0131B02'), ('P0131E00', 'P0131B03'), ('P0131E00', 'P0131B04'), ('P0131E00', 'P0131B05'), ('P0131E00', 'P0131B06'), ('P0355E00', 'P0355B03'), ('P0355E00', 'P0355B01'), ('P0355E00', 'P0355B02'), ('P0186E00', 'P0186B01'), ('P0186E00', 'P0186B02'), ('P0186E00', 'P0186B03'), ('P0186E00', 'P0186B04'), ('P0193E00', 'P0193B01'), ('P0196E00', 'P0196B01'), ('P0202E00', 'P0202B01'), ('P0233E00', 'P0233J01'), ('P0243E00', 'P0243B01'), ('P0243E00', 'P0243B02'), ('P0243E00', 'P0243B03'), ('P0249E00', 'P0249J01'), ('P0252E00', 'P0252B01'), ('P0252E00', 'P0252B02'), ('P0335E00', 'P0335RT'), ('P0335RT', 'P0335B01'), ('P0341E00', 'P0341B01'), ('P0344E00', 'P0344B01'), ('P0344E00', 'P0344B02'), ('P0345E00', 'P0345B01'), ('P0346E00', 'P0346B01'), ('P0136E00', 'P0136B01'), ('P0137E00', 'P0137B01'), ('P0137E00', 'P0137B02'), ('P0139E00', 'P0139B01'), ('P0139E00', 'P0139B02'), ('P0139E00', 'P0139B03'), ('P0139E00', 'P0139B04'), ('P0139E00', 'P0139B05'), ('P0145E00', 'P0145B01'), ('P0146E00', 'P0146B01'), ('P0146E00', 'P0146B02'), ('P0146E00', 'P0146B03'), ('P0146E00', 'P0146B04'), ('P0146E00', 'P0146B05'), ('P0146E00', 'P0146B06'), ('P0151E00', 'P0151B01'), ('P0151E00', 'P0151B02'), ('P0151E00', 'P0151B03'), ('P0162E00', 'P0162B01'), ('P0165E00', 'P0165B01'), ('P0165E00', 'P0165B02'), ('P0175E00', 'P0175B01'), ('P0175E00', 'P0175B02'), ('P0175E00', 'P0175B03'), ('P0175E00', 'P0175B04'), ('P0175E00', 'P0175B05'), ('P0177E00', 'P0177J01'), ('P0354E00', 'P0354J01'), ('P0354J01', 'P0354B01'), ('P0354J01', 'P0354B02'), ('P0354J01', 'P0354B03'), ('P0354J01', 'P0354B04'), ('P0354J01', 'P0354B05'), ('P0354J01', 'P0354B06'), ('P0252E00', 'P0252B03'), ('P0252E00', 'P0252B04'), ('P0253E00', 'P0253B01'), ('P0253E00', 'P0253B02'), ('P0253E00', 'P0253B03'), ('P0253E00', 'P0253B04'), ('P0253E00', 'P0253B05'), ('P0253E00', 'P0253B06'), ('P0253E00', 'P0253B07'), ('P0253E00', 'P0253B08'), ('P0253E00', 'P0253B09'), ('P0253E00', 'P0253B10'), ('P0261E00', 'P0261B01'), ('P0262E00', 'P0262B01'), ('P0278E00', 'P0278J01'), ('P0280E00', 'P0280B01'), ('P0280E00', 'P0280B02'), ('F000RGC', 'P0200E00'), ('P0321E00', 'P0321B01'), ('P0325E00', 'P0325B01'), ('P0325E00', 'P0325B02'), ('P0326E00', 'P0326B01'), ('P0327E00', 'P0327B01'), ('P0328E00', 'P0328B01'), ('P0329E00', 'P0329B01'), ('P0329E00', 'P0329B02'), ('P0333E00', 'P0333J01'), ('F000NT', 'P0338J01'), ('F000NT', 'F0331E00'), ('F000T', 'F0279LP'), ('F000T', 'F0331LP'), ('F0279E00', 'F0279LP'), ('F0279E00', 'F0279RT'), ('F0279G00', 'F0279LP'), ('F0331E00', 'F0331RT'), ('F0331G00', 'F0331LP'), ('P0372E00', 'P0372B01'), ('P0372E00', 'P0372B02'), ('P0372E00', 'P0372B03'), ('P0322G00', 'P0322J01'), ('P0322E00', 'P0322J01'), ('P0093E00', 'P0093B02'), ('F00YTC', 'P0129E00'), ('F00YTC', 'P0164E00'), ('P0172E00', 'P0172J01'), ('P0269E01', 'P0269B99'), ('F000T', 'P0329B99'), ('P0341E00', 'P0341B02'), ('P0345E00', 'P0345B02'), ('P0294E00', 'P0294B01'), ('P0373E00', 'P0373B01'), ('P0373E00', 'P0373B02'), ('P0313E00', 'P0313B02'), ('F000T', 'P0243B99'), ('F000T', 'P0269E01'), ('P0243E00', 'P0243B99'), ('F000RGC', 'P0207E00'), ('P0342E00', 'P0342B01'), ('P0358J01', 'P0358J02'), ('P0358J01', 'P0358RT'), ('P0359E00', 'P0359B01'), ('P0360J01', 'P0360B01'), ('P0360J01', 'P0360B02'), ('P0360J01', 'P0360D01'), ('P0362J01', 'P0362D01'), ('P0320J01', 'P0320J02'), ('P0320J01', 'P0320J03'), ('P0164E00', 'P0164B01'), ('P0269J01', 'P0269J02'), ('P0269J01', 'P0269B01'), ('P0269J01', 'P0269B02'), ('P0338E00', 'P0338J01'), ('P0269J02', 'P0269B02'), ('F0279RT', 'P0279J01'), ('P0338E00', 'P0339J01'), ('P0338J01', 'P0338B01'), ('P0338J01', 'P0339B01'), ('P0348J01', 'P0348D01'), ('P0348J01', 'P0348D02'), ('P0348J01', 'P0348D03'), ('P0336E00', 'P0336J01'), ('F0318LP', 'F0318RT'), ('F0318RT', 'P0318J01'), ('P0233J01', 'P0233J02'), ('P0249J01', 'P0249B01'), ('P0333J01', 'P0333B01'), ('P0333J01', 'P0333B02'), ('P0333J01', 'P0333B03'), ('P0337E00', 'P0337J01'), ('P0340E00', 'P0340J01'), ('P0343E00', 'P0343B01'), ('P0343E00', 'P0343B02'), ('P0343E00', 'P0343B03'), ('P0349E00', 'P0349B01'), ('P0177J01', 'P0177J02'), ('P0350E00', 'P0350B01'), ('P0351E00', 'P0351B01'), ('P0352E00', 'P0352B01'), ('P0352E00', 'P0352B02'), ('P0353E00', 'P0353B01'), ('P0278J01', 'P0278B01'), ('P0323E00', 'P0323B01'), ('P0323E00', 'P0323B02'), ('F0331LP', 'F0331RT'), ('F0331RT', 'P0331J01'), ('F0279LP', 'F0279RT'), ('P0322J01', 'P0322B01'), ('P0129E00', 'P0129B01'), ('P0129E00', 'P0129B02'), ('P0172J01', 'P0172B01'), ('P0269J01', 'P0269J03'), ('P0172J01', 'P0172B02'), ('P0207E00', 'P0207B01'), ('P0200E00', 'P0200B01'), ('P0200E00', 'P0200B02'), ('P0269J02', 'P0269J03'), ('P0358J02', 'P0358J03'), ('P0358RT', 'P0358J02'), ('P0318J01', 'P0318B01'), ('P0331J01', 'P0331B01'), ('P0331J01', 'P0331B02'), ('P0279J01', 'P0279B01'), ('P0279J01', 'P0279B02'), ('P0279J01', 'P0279B99'), ('P0339J01', 'P0339B01'), ('P0233J02', 'P0233B01'), ('P0233J02', 'P0233B02'), ('P0336J01', 'P0336B01'), ('P0337J01', 'P0337B01'), ('P0340J01', 'P0340B01'), ('P0177J02', 'P0177B01'), ('P0177J02', 'P0177B02'), ('P0320J02', 'P0320B01'), ('P0320J03', 'P0320B02'), ('P0320J03', 'P0320B03'), ('P0269J03', 'P0269B03'), ('P0358J03', 'P0358B01'), ('P0358J03', 'P0358D01')])

# creating a dictionary of options to be used in the nx.draw functoin, I still need to find out what options are accepted and _ 
    # what the difference between node_size and width is.
options = {
    'node_color': 'black',
    'node_size': 3,
    'width': 1,
}

# creating a dictionary file that contains node positions many layouts available, I chose the graphviz layout because I intend _ 
    # use graphviz to render my graph at some point due to it's ability to draw heirarchical graphs using a root and it's portability _
    # which means I can install it on my work pc without admin priviliges.
pos = nx_pydot.graphviz_layout(G, proj='dot', root='F0000PT1')

# drawing my graph to be rendered in a simple MatPlotLib window
nx.draw(G, pos=pos, with_labels=True, **options)

# writing a dot file to be, later, rendered using GraphViz in a later iteration
write_dot(G, 'IA_RELATIONSHIP.dot')

# showing the graph that was drawn above using MatPlotLib, I will need to render this in GraphViz since MatPlotLib's window is too _ 
    # small and has too much node overlap.
plt.show(G)


render('dot', 'png', 'IA_RELATIONSHIP.dot', renderer= None, formatter= None, quiet= False)

#%%
