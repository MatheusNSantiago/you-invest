def render(result):
    """Render as a html page"""
    titulo = result["titulo"]
    categoria = result["categoria"]
    pontos_chave = result["pontos_chave"]


    text = f"""
    <html>
        <head>
            <title>{titulo}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #fff;
                    border-radius: 5px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    color: #333;
                    text-align: center;
                }}
                h3 {{
                    color: #666;
                    text-align: center;
                }}
                ul {{
                    list-style-type: none;
                    padding: 0;
                }}
                li {{
                    margin-bottom: 10px;
                    padding: 10px;
                    background-color: #f9f9f9;
                    border-left: 5px solid #3498db;
                    border-radius: 3px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>{titulo}</h1>
                <h3>{categoria}</h3>
                <ul>
                    {"".join([f"<li>{ponto}</li>" for ponto in pontos_chave])}
                </ul>
            </div>
        </body>
    </html>
    """

    # <html>
    #     <head>
    #         <title>{titulo}</title>
    #     </head>
    #     <body>
    #         <h1>{titulo}</h1>
    #         </hr>
    #         <h3>{categoria}</h3>
    #         </hr>
    #         <ul>
    #             {"".join([f"<li>{ponto}</li>" for ponto in pontos_chave])}
    #         </ul>
    #     </body>
    # </html>
    # """
    open("index.html", "w").write(text)
