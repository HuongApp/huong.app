# Huong.App

A website contains some great apps for you from Huong with love.
https://huongapp.herokuapp.com/

## Run on your local workstation

```bash
# create an virtual environment and activate it
python -m venv .venv
. .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run
gunicorn huongapp:app
```
