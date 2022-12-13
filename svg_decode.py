import yaml
import urllib.parse as urlparse
import math

def decode_svg(svg) :
    new_svg = urlparse.unquote(svg) \
        .replace('url("data:image/svg+xml,', '') \
        .replace(r'\\', '') \
        .replace('");', "") \
        .replace("<?xml version='1.0' encoding='UTF-8'?>", '')
    print(new_svg)
    return new_svg

def converted_yaml():
    with open('icon_primary.yml', 'r') as stream :
        try :
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc :
            print(exc)

    converted_data = {}
    for key, value in data.items() :
        converted_data[key] = decode_svg(value)

    with open('icon_primary_converted.yml', 'w') as outfile :
        yaml.dump(converted_data, outfile, default_flow_style=False, width=math.inf)

def create_template():
    with open('boxicons.yml', 'r') as stream :
        try :
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc :
            print(exc)

    with open('template.yml', 'w') as outfile :
        for key, values in data.items():
            outfile.write(key + ":\n")

decode_svg('''url("data:image/svg+xml,%3Csvg id='Layer_1' height='100%' viewBox='0 0 24 24' width='100%' xmlns='http://www.w3.org/2000/svg' data-name='Layer 1'%3E%3Cpath d='m20.537 12.7-1.13-.7 1.131-.7a4.126 4.126 0 0 0 1.729-2.031 3.919 3.919 0 0 0 -3.28-5.272 4.124 4.124 0 0 0 -2.586.654l-.401.249v-.728a4.116 4.116 0 0 0 -3.607-4.153 4 4 0 0 0 -4.393 3.981v.9l-.4-.25a4.122 4.122 0 0 0 -2.587-.657 3.918 3.918 0 0 0 -3.283 5.27 4.123 4.123 0 0 0 1.73 2.031l1.133.706-1.131.7a4.126 4.126 0 0 0 -1.729 2.031 3.918 3.918 0 0 0 3.286 5.272 4.124 4.124 0 0 0 2.581-.651l.4-.252v.9a4 4 0 0 0 8 0v-.9l.4.251a4.126 4.126 0 0 0 2.58.653 3.918 3.918 0 0 0 3.284-5.272 4.128 4.128 0 0 0 -1.727-2.032zm-.311 4.418a1.916 1.916 0 0 1 -2.639.613l-2.059-1.282a1 1 0 0 0 -1.528.851v2.7a2 2 0 0 1 -4 0v-2.7a1 1 0 0 0 -1.528-.849l-2.059 1.284a1.915 1.915 0 1 1 -2.025-3.252l2.625-1.634a1 1 0 0 0 0-1.7l-2.625-1.633a1.915 1.915 0 0 1 2.025-3.252l2.059 1.282a1 1 0 0 0 1.528-.846v-2.593a2.075 2.075 0 0 1 1.664-2.08 2 2 0 0 1 2.336 1.973v2.7a1 1 0 0 0 1.528.848l2.059-1.281a1.915 1.915 0 1 1 2.025 3.252l-2.625 1.634a1 1 0 0 0 0 1.7l2.625 1.634a1.914 1.914 0 0 1 .614 2.638z'/%3E%3C/svg%3E");''')
