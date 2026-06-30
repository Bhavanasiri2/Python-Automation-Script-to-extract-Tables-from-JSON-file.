import json
import argparse
 
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
 
def load_target(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip().lower()
 
def normalize_id(x):
    return str(x)
 
def find_start_nodes(linked, target_substring):
    matches = []
    for nid, node in linked.items():
        name = node.get("name", "")
        if target_substring in name.lower():
            matches.append(nid)
    return matches
 
def print_simple_lineage(start_ids, linked):
    """
    Prints lineage like:
       file1 -> child1, child2
       child1 -> child3
       child2 -> (no downstream)
    """
 
    print("\n=== SIMPLE DOWNSTREAM LINEAGE ===\n")
 
    visited = set()
    stack = list(start_ids)
 
    while stack:
        nid = stack.pop()
        if nid in visited:
            continue
        visited.add(nid)
 
        node = linked[nid]
        name = node.get("name", f"(id={nid})")
 
        succ_ids = [normalize_id(s) for s in node.get("succ", []) if str(s) in linked]
 
        if succ_ids:
            succ_names = [linked[s]["name"] for s in succ_ids]
            print(f"{name}  -->  {', '.join(succ_names)}")
            # push successors to stack
            for s in succ_ids:
                stack.append(s)
        else:
            print(f"{name}  -->  (no downstream)")
 
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph", required=True)
    parser.add_argument("--target", required=True)
    args = parser.parse_args()
 
    data = load_json(args.graph)
 
    if "linked" not in data:
        raise ValueError("JSON missing 'linked' section")
 
    linked = data["linked"]
 
    target = load_target(args.target)
    start_nodes = find_start_nodes(linked, target)
 
    print("\n=== Matching Start Nodes ===")
    if not start_nodes:
        print(f"No matches for '{target}'. Try a broader substring.")
        return
 
    for s in start_nodes:
        print(f"{s} | {linked[s].get('name')}")
 
    print_simple_lineage(start_nodes, linked)
 
if __name__ == "__main__":
    main()
