import matplotlib.pyplot as plt

# Create a flowchart diagram
plt.figure(figsize=(8, 6))

# Define nodes
nodes = {
    'Start': (0, 0),
    'Purchase': (0, -1),
    'Referral': (0, -2),
    'Earn Points': (0, -3),
    'Redeem Points': (0, -4),
    'End': (0, -5),
}

# Define edges
edges = [('Start', 'Purchase'),
         ('Purchase', 'Earn Points'),
         ('Purchase', 'Referral'),
         ('Referral', 'Earn Points'),
         ('Earn Points', 'Redeem Points'),
         ('Redeem Points', 'End')]

for node, (x, y) in nodes.items():
    plt.annotate(node, (x, y), fontsize=12, ha='center', va='center', bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgray'))

for start, end in edges:
    x1, y1 = nodes[start]
    x2, y2 = nodes[end]
    plt.plot([x1, x2], [y1, y2], 'b-', linewidth=2)

plt.title('Flowchart Diagram for Proposed Feature')
plt.axis('off')
plt.show()
