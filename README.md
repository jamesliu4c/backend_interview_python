# Backend Interview Repository

This is a Python project with Flask, set up using pip-tools.

In case the workspace is brand new, fresh, do this:

```bash
pip install --upgrade pip
python -m venv env
source env/bin/activate
pip insall pip-tools
pip-compile
pip-sync
```

Once that is set up, you can run the app using simply:

```bash
flask run
```

It will tell you an address with a port forward. So now you have a working API. Then it is up to you. Have a fun interview.