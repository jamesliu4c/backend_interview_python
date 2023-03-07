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

Once that is set up, you can run the app with hot reload:

```bash
flask --debug run
```

Use httpie to make requests from the terminal easy

```bash
http :5000/campaign/ start_date=="2023-01-01" end_date=="2023-01-31"
```

It will tell you an address with a port forward. So now you have a working API. The port forward by default only works in your (interviewer) local. Click on the PORTS tab (on the bottom toolbox, next to TERMINAL), right click on the forwarded port, and select public. Note, it becomes private every time the server restarts, so keep an eye on that tab and re-publicize the port when you need. Then it is up to you. Have a fun interview.