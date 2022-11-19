from xml.dom.minidom import parse
from xml.parsers.expat import ExpatError

def xml_to_dict(xml_file):
    try:
        xml_minidom = parse(xml_file)
    except ExpatError:
        return None

    root = xml_minidom.firstChild
    xml_dict = {}
    xml_dict.update(convert_node(root))

    return xml_dict

def convert_node(node):
    if not node:
        return ""
    elif node.nodeType == 3 and node.data.strip():
        return node.data
    elif node.nodeType == 1:
        if len(node.childNodes) > 1:
            child_nodes = []
            for child_node in node.childNodes:
                node_dict = convert_node(child_node)
                if node_dict:
                    child_nodes.append(node_dict)
        else:
            child_nodes = convert_node(node.firstChild)

        return {node.nodeName: child_nodes}