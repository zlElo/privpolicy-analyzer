import json

def load_analysis(file):

    def generate_html_snippet(title, text, ranking):
        return f'''
    <div class="widget">
        <h2>{title}</h2>
        <p>{text}</p>
        <p class="ranking">Ranking: {ranking}</p>
    </div>
    '''

    def generate_widgets_html():
        widgets_html = ''
        with open(f'data/{file}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        with open(f'informations/infos.json', 'r', encoding='utf-8') as d:
            data2 = json.load(d)

        for key in data:
            text = data[key]
            title = key
            for key2 in data2:
                ranking = data2[key2]
            widget_html = generate_html_snippet(title, text, ranking)
            widgets_html += widget_html

        return widgets_html

    html_template = '''
    <!DOCTYPE html>
    <html lang="de">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Widgets</title>
    <style>
        body {{
        font-family: Arial, sans-serif;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 1rem;
        padding: 1rem;
        }}
        .widget {{
        background-color: #f0f0f0;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        padding: 1rem;
        width: 300px;
        }}
        .widget p {{
        font-size: 1rem;
        line-height: 1.5;
        }}
        .widget .ranking {{
        font-weight: bold;
        color: #f00;
        }}
    </style>
    </head>
    <body>
    {widgets}
    </body>
    </html>
    '''

    widgets_html = generate_widgets_html()
    html_output = html_template.format(widgets=widgets_html)


    func = open("src/templates/analysis.html","w")

    func.write(html_output)

    func.close()
