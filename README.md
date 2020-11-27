# Ansible Workshop Attendee List to CSV Playbook Version 2 
## What does this playbook do? 
This playbook will record down the attendees name and emails from the Ansible Wokrshop and store it in a CSV. This is then pushed into Google Sheets and shared with the email accounts that are stored **master-upload.py** python script 

## Pre-reqs
1. Make sure that the workshop is fully provionsed and that all the users have used the http://login.d98x.open.redhat.com/ page to grab their workshop credentials. 
2. You have access to the login url for the workshop for example http://login.d98x.open.redhat.com/list.php
3. Ansible and Python installed on your the machine that will be running the playbook (default is localhost). 
4. Most importantly make sure that the **client_secret.json** is in the folder that you launch the playbook from. The **client_secret.json** can be retrieved from Nasim Miah (nmiah@redhat.com).

## Running the playbook
Run the playbook as follows. 

Example for workshop environment ...

```bash
ansible-playbook list2.yml
What is the workshop URL? An example would be http://login.d98x.open.redhat.com/list.php: http://login.a76d.open.redhat.com/list.php
What is the workhop student password?: cNQn9ZxY9pAHYx
```

## Result 
attendee-list-{workshop-date}.csv 
