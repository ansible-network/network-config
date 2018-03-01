# Role Name: network-config
The ```network-config``` role provides a set of tasks for working with network
device active (running) configurations.  The role provides tasks for retrieving
the current device configuration, rendering a device configuration based on
facts and loading the the configuration onto the device.  

Any open bugs and/or feature requests are tracked in [Github issues](../../issues).

Interested in contributing to this role, please see [CONTRIBUTING](CONTRIBUTING.md)

## Requirements
None

## Role Tasks
The following are the available tasks provided by this role for use in
playbooks.

* get [[source]](tasks/get.yaml) [[docs]](docs/get.md)
* backup [[source]](tasks/backup.yaml) [[docs]](docs/backup.md)

## Role Variables
The following role variables are defined by this role.

### ansible_network_os
Configure the network os value for the network device.  This role variable is
used to map the role actions to device specific provider implementations.
Typically this value should be set in the playbook inventory for the host.  

### backup_path
Configures the path to be used to store configuration backups.  If the path
specified by this role variable does not exist, the role will automatically
attempt to create the directory.  

The default value is ```{{ playbook_dir }}/backups```

### filename
This role variable is used to determine the name of the file to be written to
disk that contains the device configuration.  This role variable is appended to
the backup path to generate the full path to the backed up configuration.

The default value is ```{{ inventory_hostname_short }}.cfg```

## Modules
The following is a list of modules that are provided by this role.

None

## Plugins
The following is a list of plugins that are provided by this role.

None

## Dependencies
The following is the list of dependencies on other roles this role requires.

* [network-engine](http://github.com/ansible-network/network-engine)

## License
GPLv3

## Author Information
Ansible Network Engineering Team
