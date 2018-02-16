# Task get
The ```get``` task can be used to retrieve the current active (running)
configuration from the network device.  The ```get``` task implements a set of
tasks providers that are based on the value of the ```ansible_network_os```
fact.  

The ```get``` tasks will first check if the ```ansible_network_os``` fact has
been configured and, if it has not been configured, it will set the value to
default.

The task will then include the set of platform specific tasks in order to
retrieve the current device running configuration.  The task will look for the
the platform specific tasks using the following order:

1) {{ playbook_dir }}/providers/{{ ansible_network_os }}/network-config/get.yaml
2) {{ role_path }}/providers/{{ ansible_network_os }}/get.yaml
3) /etc/ansible/network/{{ ansible_network_os }}/network-config/get.yaml

If the task is unable to find a sutable module in one of the preceeding
locations, the ```get``` task will error.

## Requirements
The following is the list of requirements for using the this task:

* Ansible 2.5 or later
* Connection ```network_cli```

## Suppported providers
This task includes providers for the following set of providers:

* asa
* eos
* ios
* iosxr
* junos
* nxos
* vyos

## Adding additional platform support
The ```get``` task can be extended to support additional network devices by
provider providers that return the device configuration.  In order to provide
support for additional platforms, simply add the ```get.yaml``` tasks in once
of the search locations and the role will automatically find it.

## Arguments
The ```get``` task has no configurable arguments.

## Notes
None

## Changelog

* 2.5.0 - initial task added to the role

