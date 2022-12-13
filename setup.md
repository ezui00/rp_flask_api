G:\>dir
 Volume in drive G is Google Drive
 Volume Serial Number is 1983-1116

 Directory of G:\

30-Nov-22  15:11    <DIR>          My Drive
30-Nov-22  15:11    <DIR>          Other computers
               0 File(s)              0 bytes
               2 Dir(s)  25.476.505.600 bytes free

G:\>cd "My Drive"

G:\My Drive>cd @python3

G:\My Drive\@python3>cd rp_flask_api

G:\My Drive\@python3\rp_flask_api>**python -m venv venv1**

G:\My Drive\@python3\rp_flask_api>
G:\My Drive\@python3\rp_flask_api>**.\venv1\Scripts\activate**

(venv1) G:\My Drive\@python3\rp_flask_api>**python -m pip install Flask==2.2.2**
Collecting Flask==2.2.2
  Downloading Flask-2.2.2-py3-none-any.whl (101 kB)
     |████████████████████████████████| 101 kB 2.2 MB/s
Collecting click>=8.0
  Downloading click-8.1.3-py3-none-any.whl (96 kB)
     |████████████████████████████████| 96 kB 1.5 MB/s
Collecting itsdangerous>=2.0
  Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)
Collecting Jinja2>=3.0
  Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
     |████████████████████████████████| 133 kB 6.4 MB/s
Collecting Werkzeug>=2.2.2
  Downloading Werkzeug-2.2.2-py3-none-any.whl (232 kB)
     |████████████████████████████████| 232 kB 6.8 MB/s
Collecting importlib-metadata>=3.6.0; python_version < "3.10"
  Downloading importlib_metadata-5.1.0-py3-none-any.whl (21 kB)
Collecting colorama; platform_system == "Windows"
  Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.1.1-cp38-cp38-win32.whl (16 kB)
Collecting zipp>=0.5
  Downloading zipp-3.11.0-py3-none-any.whl (6.6 kB)
Installing collected packages: colorama, click, itsdangerous, MarkupSafe, Jinja2, Werkzeug, zipp, importlib-metadata, Flask
Successfully installed Flask-2.2.2 Jinja2-3.1.2 MarkupSafe-2.1.1 Werkzeug-2.2.2 click-8.1.3 colorama-0.4.6 importlib-metadata-5.1.0 itsdangerous-2.1.2 zipp-3.11.0
WARNING: You are using pip version 20.1.1; however, version 22.3.1 is available.
You should consider upgrading via the 'G:\My Drive\@python3\rp_flask_api\venv1\Scripts\python.exe -m pip install --upgrade pip' command.

(venv1) G:\My Drive\@python3\rp_flask_api>dir
 Volume in drive G is Google Drive
 Volume Serial Number is 1983-1116

 Directory of G:\My Drive\@python3\rp_flask_api

04-Dec-22  18:01    <DIR>          .
04-Dec-22  17:59    <DIR>          ..
04-Dec-22  18:01    <DIR>          venv1
               0 File(s)              0 bytes
               3 Dir(s)  25.476.505.600 bytes free

(venv1) G:\My Drive\@python3\rp_flask_api>**venv1\Scripts\python.exe -m pip install --upgrade pip**
Collecting pip
  Using cached pip-22.3.1-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 20.1.1
    Uninstalling pip-20.1.1:
      Successfully uninstalled pip-20.1.1
Successfully installed pip-22.3.1

(venv1) G:\My Drive\@python3\rp_flask_api>python -m pip install "connexion[swagger-ui]==2.14.1"
Collecting connexion[swagger-ui]==2.14.1
  Downloading connexion-2.14.1-py2.py3-none-any.whl (95 kB)
     ---------------------------------------- 95.1/95.1 kB 2.7 MB/s eta 0:00:00
Requirement already satisfied: itsdangerous>=0.24 in g:\my drive\@python3\rp_flask_api\venv1\lib\site-packages (from connexion[swagger-ui]==2.14.1) (2.1.2)
Collecting packaging>=20
  Using cached packaging-21.3-py3-none-any.whl (40 kB)
Collecting requests<3,>=2.9.1
  Using cached requests-2.28.1-py3-none-any.whl (62 kB)
Collecting jsonschema<5,>=2.5.1
  Downloading jsonschema-4.17.3-py3-none-any.whl (90 kB)
     ---------------------------------------- 90.4/90.4 kB 5.0 MB/s eta 0:00:00
Collecting PyYAML<7,>=5.1
  Downloading PyYAML-6.0-cp38-cp38-win32.whl (140 kB)
     ---------------------------------------- 140.4/140.4 kB ? eta 0:00:00
Collecting clickclick<21,>=1.2
  Downloading clickclick-20.10.2-py2.py3-none-any.whl (7.4 kB)
Requirement already satisfied: flask<3,>=1.0.4 in g:\my drive\@python3\rp_flask_api\venv1\lib\site-packages (from connexion[swagger-ui]==2.14.1) (2.2.2)
Collecting inflection<0.6,>=0.3.1
  Downloading inflection-0.5.1-py2.py3-none-any.whl (9.5 kB)
Requirement already satisfied: werkzeug<3,>=1.0 in g:\my drive\@python3\rp_flask_api\venv1\lib\site-packages (from connexion[swagger-ui]==2.14.1) (2.2.2)
Collecting swagger-ui-bundle<0.1,>=0.0.2
  Downloading swagger_ui_bundle-0.0.9-py3-none-any.whl (6.2 MB)
     ---------------------------------------- 6.2/6.2 MB 7.5 MB/s eta 0:00:00
Requirement already satisfied: click>=4.0 in g:\my drive\@python3\rp_flask_api\venv1\lib\site-packages (from clickclick<21,>=1.2->connexion[swagger-ui]==2.14.1) (8.1.3)
Requirement already satisfied: importlib-metadata>=3.6.0 in g:\my drive\@python3\rp_flask_api\venv1\lib\site-packages (from flask<3,>=1.0.4->connexion[swagger-ui]==2.14.1) (5.1.0)
Requirement already satisfied: Jinja2>=3.0 in g:\my drive\@python3\rp_flask_api\venv1\lib\site-packages (from flask<3,>=1.0.4->connexion[swagger-ui]==2.14.1) (3.1.2)
Collecting pkgutil-resolve-name>=1.3.10
  Downloading pkgutil_resolve_name-1.3.10-py3-none-any.whl (4.7 kB)
Collecting pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0
  Downloading pyrsistent-0.19.2-cp38-cp38-win32.whl (60 kB)
     ---------------------------------------- 60.3/60.3 kB ? eta 0:00:00
Collecting attrs>=17.4.0
  Downloading attrs-22.1.0-py2.py3-none-any.whl (58 kB)
     ---------------------------------------- 58.8/58.8 kB 3.2 MB/s eta 0:00:00
Collecting importlib-resources>=1.4.0
  Downloading importlib_resources-5.10.0-py3-none-any.whl (34 kB)
Collecting pyparsing!=3.0.5,>=2.0.2
  Using cached pyparsing-3.0.9-py3-none-any.whl (98 kB)
Collecting charset-normalizer<3,>=2
  Using cached charset_normalizer-2.1.1-py3-none-any.whl (39 kB)
Collecting certifi>=2017.4.17
  Using cached certifi-2022.9.24-py3-none-any.whl (161 kB)
Collecting urllib3<1.27,>=1.21.1
  Downloading urllib3-1.26.13-py2.py3-none-any.whl (140 kB)
     ---------------------------------------- 140.6/140.6 kB 8.7 MB/s eta 0:00:00
Collecting idna<4,>=2.5
  Using cached idna-3.4-py3-none-any.whl (61 kB)
Requirement already satisfied: MarkupSafe>=2.1.1 in g:\my drive\@python3\rp_flask_api\venv1\lib\site-packages (from werkzeug<3,>=1.0->connexion[swagger-ui]==2.14.1) (2.1.1)
Requirement already satisfied: colorama in g:\my drive\@python3\rp_flask_api\venv1\lib\site-packages (from click>=4.0->clickclick<21,>=1.2->connexion[swagger-ui]==2.14.1) (0.4.6)
Requirement already satisfied: zipp>=0.5 in g:\my drive\@python3\rp_flask_api\venv1\lib\site-packages (from importlib-metadata>=3.6.0->flask<3,>=1.0.4->connexion[swagger-ui]==2.14.1) (3.11.0)
Installing collected packages: urllib3, PyYAML, pyrsistent, pyparsing, pkgutil-resolve-name, inflection, importlib-resources, idna, charset-normalizer, certifi, attrs, swagger-ui-bundle, requests, packaging, jsonschema, clickclick, connexion
Successfully installed PyYAML-6.0 attrs-22.1.0 certifi-2022.9.24 charset-normalizer-2.1.1 clickclick-20.10.2 connexion-2.14.1 idna-3.4 importlib-resources-5.10.0 inflection-0.5.1 jsonschema-4.17.3 packaging-21.3 pkgutil-resolve-name-1.3.10 pyparsing-3.0.9 pyrsistent-0.19.2 requests-2.28.1 swagger-ui-bundle-0.0.9 urllib3-1.26.13

(venv1) G:\My Drive\@python3\rp_flask_api>**python -m pip install "flask-marshmallow[sqlalchemy]==0.14.0"**