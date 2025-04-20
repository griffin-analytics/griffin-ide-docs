from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='MMM UML Diagram', format='png')

# General graph attributes
dot.attr(rankdir='LR', size='12,8', nodesep='1', ranksep='1', pad='0.5')  # Left-to-right layout

# Define node styles
dot.attr('node', shape='rect', style='filled', fontname='Arial', fontsize='12', margin='0.3')

# Subgraphs for logical grouping
with dot.subgraph(name='cluster_input') as c:
    c.attr(label='Input')
    c.attr(color='#AEC6CF', style='filled')
    c.node('data_input', 'Data input\n- Marketing costs\n- Client Sales\n- User behaviour variables', shape='rect')

with dot.subgraph(name='cluster_preparation') as c:
    c.attr(label='Data Preparation')
    c.attr(color='#FDFD96', style='filled')
    c.node('data_preparation', 'Data preparation\n- Geometric adstock\n- Saturation transformation\n- Control Variables', shape='rect')

with dot.subgraph(name='cluster_modeling') as c:
    c.attr(label='Modeling')
    c.attr(color='#FFB347', style='filled')
    c.node('modeling', 'Modeling\n- Bayesian Analytics\n- PyMC\n- MMM', shape='rect')

with dot.subgraph(name='cluster_output') as c:
    c.attr(label='Output')
    c.attr(color='#FF6961', style='filled')
    c.node('output', 'Output\n- Dashboard\n- Recommendations', shape='rect')

# Standalone nodes
dot.node('algorithms', 'Algorithms\n- Prophet', fillcolor='#77DD77')
dot.node('environment', 'Environment\n- Colab, Vertex AI', fillcolor='#B39EB5')
dot.node('visualisation', 'Visualisation\n- PowerBI / Streamlit', fillcolor='#F49AC2')

# Connections
dot.edge('data_input', 'data_preparation', label='Data flow', fontsize='10')
dot.edge('data_preparation', 'modeling', label='Processed data')
dot.edge('modeling', 'output', label='Insights')
dot.edge('data_preparation', 'algorithms', label='Trend analysis')
dot.edge('data_preparation', 'environment', label='Execution environment')
dot.edge('modeling', 'environment')
dot.edge('output', 'visualisation', label='Display')
dot.edge('algorithms', 'modeling', label='Algorithm input')  # Added edge from Prophet (Algorithms) to Modeling

# Render and display the diagram
dot.render('Enhanced_MMM_UML', view=True)

from IPython.display import Image
Image('Enhanced_MMM_UML.png')
