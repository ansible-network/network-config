# Get
The ```get``` task can be used to retrieve the current active (running)
configuration from the network device.  The ```get``` task implements a set of
tasks providers that are based on the value of the ```ansible_network_os```
fact.  

## How to retrieve the current device configuration
In order to retrieve the current device configuration simply import this action
in the playbook and the current active (running) configuration will be
retrieved from the host.  

```
---
- hosts: all
  
  tasks:
    - name: backup all configurations
      import_role:
        name: network-config
        tasks_from: get
```

The contents of the configuration will be available in the host fact
```configuration```.  In order to see the contents of the configuration on the
console, use the [debug](http://http://docs.ansible.com/ansible/latest/debug_module.html) 
module.

```
---
- hosts: all
  
  tasks:
    - name: backup all configurations
      import_role:
        name: network-config
        tasks_from: get

    - debug: var=configuration.text
```


## How to change the configuration output format
Some network devices support returning the configuration in different output
formats.  For instance, JUNOS based devices can return the configuration as
text (junos format), xml or set.  If you need to change the format of the
device configuration output, set the ```config_format``` variable for that
host.

This action will automatically load platform specific variables.  It searchs
for variable files to inlcude when the task is executed.  Platform specific
variables are loaded based on precedence.  

The action will attempt to find and load platform specific variables in the
following order:

* ```{{ playbook_dir }}/vars/network_config/{{ ansible_network_os }}.yaml``` 
* ```/etc/ansible/network/network_config/{{ ansible_network_os }}.yaml``` 
* ```{{ role_path }}/vars/{{ ansible_network_os }}.yaml``` 


## Requirements
The following is the list of requirements for using the this task:

* Ansible 2.5 or later

## Arguments
The ```get``` task has no configurable arguments.

## Notes
None

## Changelog

* 2.5.0 - initial task added to the role

