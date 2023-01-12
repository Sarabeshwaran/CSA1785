Input:

def map_coloring(colors, domains, neighbors, assignments):
    if len(assignments) == len(domains):
        return assignments
    unassigned = get_unassigned_variable(domains, assignments)
    for color in colors:
        if is_consistent(unassigned, color, neighbors, assignments):
            assignments[unassigned] = color
            result = map_coloring(colors, domains, neighbors, assignments)
            if result is not None:
                return result
            del assignments[unassigned]
    return None

def get_unassigned_variable(domains, assignments):
    for variable in domains:
        if variable not in assignments:
            return variable

def is_consistent(variable, color, neighbors, assignments):
    for neighbor in neighbors[variable]:
        if neighbor in assignments and assignments[neighbor] == color:
            return False
    return True

# Example usage:
if __name__ == '__main__':
    colors = ['red', 'green', 'blue']
    domains = {'WA': ['red', 'green', 'blue'], 'NT': ['red', 'green', 'blue'], 'Q': ['red', 'green', 'blue'], 'NSW': ['red', 'green', 'blue'], 'V': ['red', 'green', 'blue'], 'SA': ['red', 'green', 'blue'], 'T': ['red', 'green', 'blue']}
    neighbors = {'WA': ['NT', 'SA'], 'NT': ['WA', 'Q', 'SA'], 'SA': ['WA', 'NT', 'Q', 'NSW', 'V'], 'Q': ['NT', 'SA', 'NSW'], 'NSW': ['Q', 'V', 'SA'], 'V': ['NSW', 'SA'], 'T': []}
    assignments = {}
    result = map_coloring(colors, domains, neighbors, assignments)
    print(result)

Output:
  
{'WA': 'red', 'NT': 'green', 'Q': 'red', 'NSW': 'green', 'V': 'red', 'SA': 'blue', 'T': 'red'}
