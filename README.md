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
![Alt text](https://drive.google.com/file/d/15sdIW2tR0UJP-u1nWt91hEMyu4E9Bso4/view?usp=sharing?raw=true "Title")  
