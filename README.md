# HeyPy

A flask application for reviewing best DevSecOps practices with GitHub Workflows and Actions.

## Run heypy

### From command line

Using environment vars

```sh
export FLASK_APP=heyapp:create_app
export FLASK_CONFIG=production
flask -run
```

Gunicorn

```sh
gunicorn --bind 0.0.0.0:8080 --log-level debug heyapp:create_app 
```

To run your application with a specific configuration:

Set an environment variable:

```sh
export FLASK_CONFIG=production
flask --app yourapplication run
```

(Or set FLASK_CONFIG=production on Windows)

Pass it directly to create_app (e.g., for testing):

```Python
    app = create_app('testing')
```

This class-based approach with environment variables is the most robust and secure way to manage configuration in Flask applications.
