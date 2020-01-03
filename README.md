# NASA_APoD
A flask application that displays the APoD and also gives you an option to download the pdf version (with description)

# Usage  
* clone this repo and start a virualenv such that the directory looks like this :
```
APoD_app/
  venv/
  app/
    __init__.py
    routes.py
    templetes/
      error_file.html
      home.html
  apod_app.py
  get_pdf.py

```
* Then run the following command to setup the environment variable
```
(venv) $ export FLASK_APP=microblog.py
```
* Next run this command to begin the local server :
```
(venv) $ flask run
```
* Then you will see a webpage like this :
<a href="https://drive.google.com/uc?export=view&id=15sdIW2tR0UJP-u1nWt91hEMyu4E9Bso4"><img src="https://drive.google.com/uc?export=view&id=15sdIW2tR0UJP-u1nWt91hEMyu4E9Bso4" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>
* Then fill the text box with your required date and submit
* You will get a preview and also an option to download as pdf (contains description)
