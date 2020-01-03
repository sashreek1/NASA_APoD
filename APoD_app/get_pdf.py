import pdfkit

def get_pdf (img_url,description):
    html_str = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>APOD download</title>
        <style>
    img {
        text-align: center;
    }
    p {
    margin-top: 100px;
    margin-bottom: 100px;
    margin-right: 150px;
    margin-left: 80px;
    }
    </style>
    
    </head>
    <body>
        <div style="margin-top:80px">
        <center>
            <img src= """+img_url+""" alt="NASA APoD" height="600px">
        </center>
        </div>
    <font face="times new roman" size='16'>
        <p> """ +description+"""
    </p></font>
    </body>
    </html>
    """
    f = open("app/out.html", "w")
    f.write(html_str)
    f.close()
    pdfkit.from_file('app/out.html', 'app/out.pdf')
