# Get
The ```get``` task can be used to retrieve the current active (running)
configuration from the network device.  The ```get``` task implements a set of
tasks providers that are based on the value of the ```ansible_network_os```
fact.  

After the device configuration is retrieved, this task will attempt to parse
the configuration into a set of Ansible facts.  The parsing is based on a set
of parser files that are embebbed int he ```files/parsers``` directory in this
role.  

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
    - debug: var=ansible_network_config
```

## How to disable the automatic config parser
In some instanced, it may be desirable to disable to the automatic parsing of
the configuration  file.  In order to disable the parsing function, set the
role variable ```enable_config_parser``` to ```False```.

```
---
- hosts: all
  
  tasks:
    - name: backup all configurations
      import_role:
        name: network-config
        tasks_from: get
      vars:
        enable_config_parser: no

    - debug: var=configuration.text
    - debug: var=ansible_network_config
```

## Requirements
The following is the list of requirements for using the this task:

* Ansible 2.5 or later
* Ansible network-engine role

## Arguments
The ```get``` task has no configurable arguments.

## Notes
None

## Changelog

* 2.5.0 - initial task added to the role

