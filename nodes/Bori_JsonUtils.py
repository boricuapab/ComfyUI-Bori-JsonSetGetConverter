from pathlib import Path

def gather_files(dir):
    return [f for f in Path(dir).iterdir() if f.is_file() and f.suffix == ".json"]

def set_node(node, props):
    return {
        "id": node["id"],
        "type": "SetNode",
        "pos": node["pos"],
        "size": node["size"],
        "flags": {"collapsed": True},
        "order": node["order"],
        "mode": 0,
        "inputs": [{
            "name": node["inputs"][0]["type"],
            "type": node["inputs"][0]["type"],
            "link": node["inputs"][0]["link"],
        }],
        "outputs": [{
            "name": "*",
            "type": "*",
            "links": []
        }],
        "title": "Set_" + str(node["widgets_values"][0]),
        "properties": {},
        "widgets_values": node["widgets_values"],
    }

def get_node(node, props):
    return {
        "id": node["id"],
        "type": "GetNode",
        "pos": node["pos"],
        "size": node["size"],
        "flags": {"collapsed": True},
        "order": node["order"],
        "mode": 0,
        "inputs": [],
        "outputs": [{
            "name": props["type"],
            "type": props["type"],
            "links": node["outputs"][0]["links"]
        }],
        "title": "Get_" + str(node["widgets_values"][0]),
        "properties": {},
        "widgets_values": node["widgets_values"],
    }
