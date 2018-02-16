# Backup

The purpose of this action is to perform backups of the current active
(running-config) configuration of the device.  The ```backup``` action will
attach to each device, grab a copy of the device configuration and save that
configuration file to the backup path.

## How to perform a backup
To use this role, simply import the role and execute the backup tasks.  Here is
an example playbook that implements the backup role.

```
---
- hosts: all
  
  tasks:
    - name: backup all configurations
      import_role:
        name: network-config
        tasks_from: backup
```

By default, the backup role will create a directory called ```backups``` in 
the current playbook directory and place all device configurations there.

The backup file will only be updated on disk if the contents have changed.  

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

