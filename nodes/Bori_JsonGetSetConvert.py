import os
import json
import random
from pathlib import Path

from .Bori_JsonUtils import gather_files, set_node, get_node

class Bori_JsonGetSetConvert:

    @classmethod
    def INPUT_TYPES(cls):
        
        return {"required": {
                    "json_folder": ("STRING", {"default": "C:/comfyADMDLoraTrain/ComfyUI/custom_nodes/ComfyUI-Bori-JsonSetGetConverter/convert"}),
                    }
                }

    RETURN_TYPES = ()
#   RETURN_NAMES = ()
    FUNCTION = "convert_folder"
    OUTPUT_NODE = True
    CATEGORY = "Bori_Converter"

    def convert_folder (self, json_folder):
#        def gather_files(dir):
#           return [f for f in Path(dir).iterdir() if f.is_file() and f.suffix == '.json']
        files = gather_files(json_folder)
        for json_path in files:
            with open(json_path, encoding="utf8") as f:
                data = json.load(f)

            get_nodes = []
            set_nodes = []

            for node in data["nodes"]:
                if node["type"] == "mape Variable":
                    value = node["widgets_values"][0]
                    link = node["inputs"][0]["link"]

                    if link is not None:
                        # This is a Set node
                        set_nodes.append({
                            "value": value,
                            "id": node["id"],
                            "pos": node["pos"],
                            "type": node["inputs"][0]["type"]
                        })
                    else:
                        # This is a Get node
                        get_nodes.append({
                            "value": value,
                            "id": node["id"]
                        })

            # Replace nodes by ID
            id_to_node = {n["id"]: n for n in data["nodes"]}
            new_nodes = []

            for node in data["nodes"]:
                if node["type"] == "mape Variable":
                    value = node["widgets_values"][0]
                    node_id = node["id"]

                    # Check if this is a Set
                    match = next((s for s in set_nodes if s["id"] == node_id), None)
                    if match:
                        print(f"Replacing node {node_id} with {'Set' if match else 'Get'} node for value: {value}")
                        new_node = set_node(node, match)
                        new_nodes.append(new_node)
                        continue

                    # Check if this is a Get
                    match = next((g for g in get_nodes if g["id"] == node_id), None)
                    if match:
                        # Match the Get with the correct Set for its value
                        set_match = next((s for s in set_nodes if s["value"] == match["value"]), None)
                        if set_match:
                            print(f"Replacing node {node_id} with {'Set' if match else 'Get'} node for value: {value}")
                            new_node = get_node(node, set_match)
                            new_nodes.append(new_node)
                            continue

                # All other nodes
                new_nodes.append(node)

            data["nodes"] = new_nodes
            
            with open(json_path, "w", encoding = "utf8") as f:
                json.dump(data, f, indent=4)

        return {}