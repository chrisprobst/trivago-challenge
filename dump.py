import csv
import json
from dataclasses import fields

import dicttoxml
import yaml
from jinja2 import Template

from hotel import Hotel


def dump_xml(data, f):
    b = dicttoxml.dicttoxml(data,
                            custom_root='hotels',
                            attr_type=False,
                            item_func=lambda _: 'hotel')
    f.write(b.decode('utf-8'))


def dump_csv(data, f):
    writer = csv.DictWriter(f, fieldnames=[field.name for field in fields(Hotel)])
    writer.writeheader()
    for d in data:
        writer.writerow(d)


def dump_html(data, f):
    template = Template(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Hotels</title>
            <style>
                .label {
                    color: #555555;
                }
            </style>
        </head>
        <body>
        <ol>
            {% for hotel in hotels %}
            <li>
                <span class="label">Name:</span> <strong>{{ hotel.name }}</strong> |
                <span class="label">Address:</span> <strong>{{ hotel.address }}</strong> | 
                <span class="label">Stars:</span> <strong>{{ hotel.stars }}</strong> |
                <span class="label">Contact:</span> <strong>{{ hotel.contact }}</strong> | 
                <span class="label">Phone:</span> <strong>{{ hotel.phone }}</strong> |
                <a href="{{ hotel.uri }}">Website</a></li>
            {% endfor %}
        </ol>
        </body>
        </html>""")

    f.write(template.render(hotels=data))


def dump_xaml(data, f):
    return yaml.dump(data, f, default_flow_style=False)


# All allowed output codecs are stored here
# To support a new output codec, simply add a new entry which satisfies the following convention:
# 'extension' => lambda data, file_handle: ...
# It will be used automatically based on the output file name
codecs = {
    '.json': json.dump,
    '.csv': dump_csv,
    '.xml': dump_xml,
    '.html': dump_html,
    '.yaml': dump_xaml,
}
