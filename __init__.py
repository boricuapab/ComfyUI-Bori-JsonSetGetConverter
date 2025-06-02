
from .nodes.Bori_JsonGetSetConvert import *

NODE_CLASS_MAPPINGS = {
    # Add mappings here
    "Bori Json Get Set Convert": Bori_JsonGetSetConvert,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Bori Json Get Set Convert": "Bori Json Get Set Convert", 
}

print ("\033[38;5;123m")
print ("Bori Json Mape To Get/Set Converter")
print ("\033[38;5;183m")
print ("Loaded")
print ("\033[0m")

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]