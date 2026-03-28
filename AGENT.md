# SETUP
vytvoření venv ve složce .venv pokud neexistuje
python -m venv .venv

aktivování venv
.\.venv\Scripts\activate

instalace pip-tools pro instalaci knihoven
python -m pip install --upgrade pip
python -m pip install pip-tools

kompilace knihoven z requirementů
python -m piptools compile requirements.in

instalace zkompilovaných knihoven
python -m pip install -r requirements.txt

