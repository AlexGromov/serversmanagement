## DESCRIPTION

ServersManagement - "mini-jenkins", allows to run scripts on remote servers via WebUI.

In current time tool has only 2 tasks that allows to deploy/clean OpenStask Fuel node.

## ACRH:

WebUI - Flask with plugins
DB - SQLAlchemy - MySQL
Remote executor - Fabric

Steps:

app login -> openid provider -> app -> task -> run -> "EXECUTOR" -> save/show results

where "EXECUTOR" may be one of:
- python.subprocess -> Fabfic -> bash script with args (current implementation)
- python.subprocess -> Fabfic with args 
- API Fabric with args
- API Jenkins with args
- ansible/etc ?

## FAQ

Why wouldn't you use "Jenkins" ?

- can't simple and flexible customize job as we want

- can't check some server's state/args/etc BEFORE run job

## INSTALL

- create mysql user/grants
<pre>
create database <db_name>;
GRANT ALL PRIVILEGES ON <db_name>.* TO '<db_user>'@'<host>' IDENTIFIED BY '<password>' WITH GRANT OPTION;
flush privileges;
cd tools; ./create_db.py
</pre>

- add user and user on remote servers

- generate ssh key

<pre>
ssh-keygen
</pre>

- copy ssh pub keys to servers

<pre>
ssh-copy-id <user>@<server>
</pre>

- setup software

<pre>
git clone https://github.com/greatehop/serversmanagement
cd serversmanagement
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
</pre>

- edit settings.py

- run configurator for "(deploy/clean)_mos" task's script
TODO: need add details

- run app
TODO: need add details

## TODO

- find and fix all issues

<pre>
grep -r 'TODO' ./
</pre>
