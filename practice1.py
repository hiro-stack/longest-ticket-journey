import re
from collections import defaultdict

class Application:
    def __init__(self):
        self.graph = defaultdict(list)
        self.max_dist = 0
        self.max_path = []
        self.all_nodes = set()

    def read_input(self):
        while True:
            try:
                line = input()
                if not line.strip():
                    break
                parts = re.split(r"\s*,\s*", line.strip())
                if len(parts) != 3:
                    continue
                u, v, d = int(parts[0]), int(parts[1]), float(parts[2])
                self.graph[u].append((v, d))
                self.all_nodes.update([u, v])
                if v not in self.graph:
                    self.graph[v] = []
            except EOFError:
                break
            except Exception:
                continue

    def dfs(self, node, visited, path, distance):
        visited.add(node)
        path.append(node)
        if distance > self.max_dist:
            self.max_dist = distance
            self.max_path = path[:]
        for neighbor, dist in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, path, distance + dist)
        visited.remove(node)
        path.pop()

    def find_longest_path(self):
        for start in self.all_nodes:
            self.dfs(start, set(), [], 0)

    def output_result(self):
        for station in self.max_path:
            print(station, end='\r\n')

    def run(self):
        self.read_input()
        self.find_longest_path()
        self.output_result()

def main():
    app = Application()
    app.run()

if __name__ == "__main__":
    main()
