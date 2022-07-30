# YouTrack ansible role
[![Molecule](https://github.com/oukooveu/ansible-role-youtrack/actions/workflows/molecule.yml/badge.svg)](https://github.com/oukooveu/ansible-role-youtrack/actions/workflows/molecule.yml)

Role to install Jetbrains YouTrack project management platform.

YouTrack is installed from JAR file as this described [here](https://www.jetbrains.com/help/youtrack/server/Install-YouTrack-JAR-as-Service-Linux.html).

## Requirements

JRE version greater than 11 should be installed.

## Role Variables

Most important options are listed below for whole list please examine defaults/main.yml.

`youtrack_version`: YourTrack version to install (default is '2021.3.29124');

`youtrack_create_user`: Create or not dedicated user unless `true` user should exist (default is `true`);

`youtrack_restore_backup`: Restore YourTrack from given backup file, all data will be removed, use this with caution (default is `false`);

`youtrack_startup_options`: String which is appended to YourTrack startup command;

`youtrack_jvm_options`: YouTrack JVM options, only system properties are supported, check [this](https://www.jetbrains.com/help/youtrack/server/YouTrack-Java-Start-Parameters.html#general-parameters) for the list;

`youtrack_env_options`: YouTrack startup options (are passed through command line arguments, list of available options could be found [here](https://www.jetbrains.com/help/youtrack/server/YouTrack-Java-Start-Parameters.html#environmental-parameters).


## Example Playbook

```
- name: install youtrack
  hosts: all
  vars:
    youtrack_version: '2022.2.51836'
  roles:
    - role: oukooveu.youtrack
```

### Molecule tests

To run tests locally:
```
python -m venv .venv
. .venv/bin/activate
pip install -r molecule/default/requirements.txt
molecule test
```
If you just want to run YouTrack this can be done by changing last command to `molecule converge`. To cleanup test environment run `molecule destroy`.

## License

Apache 2.0
