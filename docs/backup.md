# Backup
This action will backup the current active (running) configuration from
network devices.  The action will retrieve the current active configuration
and write it to the local Ansible controller in the ```backups``` folder found
in the playbook droot directory.  If the file contents have not changed since 
the last backup, then the file will not be updated.

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

## How to change the backup folder destination
Here is an example playbook that shows to to change the backup destination
folder when using the backup action.  The below example will sort the 
backup files into subfolders based on the value of the ansible_network_os 
variable.

```
---
- hosts: all
  
  tasks:
    - name: backup all configurations
      import_role:
        name: network-config
        tasks_from: backup
      vars:
        backup_path: "backups/{{ ansible_network_os }}"
```

## How to change the backup filename
By default, each host will write a file based on its inventory hostname in the
backup folder path.  The default template for the filename can be changed to 
something else in needed.  

Here is an example of that will append "-running" to the filename
```
---
- hosts: all
  
  tasks:
    - name: backup all configurations
      import_role:
        name: network-config
        tasks_from: backup
      vars:
        backup_filename: "{{ inventory_hostname_short }}-running.cfg"
```

## Requirements
The following is the list of requirements for using the this task:

* Ansible 2.5 or later

## Variables

### backup_path
The ```backup_path``` defines the location to store a copy of the device
configuration on the local Ansible controller.  This variable can be provided
as either relative to the playbook root directory or as an absolute value.

The default value is ```{{ playbook_dir }}/backups```

### backup_filename
The ```backup_filename``` defines the name of the file to write out for each
host.  After the current host configuration is retrieved, the contents are
written to disk in the [backup_path](#backup_path) using this filename.

The default value is ```{{ inventory_hostname_short }}.cfg```

## Notes
None

## Changelog
* 2.5.0 - initial task added to the role

