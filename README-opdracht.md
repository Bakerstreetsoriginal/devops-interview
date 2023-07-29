#Devops oefening

##Prerequisites

##Ansible playbooks
- These commands should all be run from the vagrant environment
- The playbooks should be run in order of the readme.
- the playbooks are located in /projects

###docker-playbook.yml
To run the docker-playbook.yml you can use the following command
>ansible-playbook docker-playbook.yml

###os-playbook.yml
To run the os-playbook.yml you can use the following command
>ansible-playbook os-playbook.yml

###helloworld-playbook
To run the helloworld-playbook.yml you can use the following command
>ansible-playbook helloworld-playbook.yml

After the playbook is up you can confirm the container is running by doing
>curl localhost:8080

the response should be
>Hello World!

##Python script
To run the python script, move into /projects/lights and run
>python3 shouldTheLightsBeOn.py