# YouTrack ansible role
[![Molecule](https://github.com/oukooveu/ansible-role-youtrack/actions/workflows/molecule.yml/badge.svg)](https://github.com/oukooveu/ansible-role-youtrack/actions/workflows/molecule.yml)

Role to install Jetbrains YouTrack project management platform.

## Important considerations

- YouTrack is installed from ZIP archive and only this option is supported.
- Don't forget to create backup before any upgrade.
- Please check [upgrade path](https://www.jetbrains.com/help/youtrack/server/Upgrade-YouTrack-ZIP.html#upgrade-matrix) before upgrading from one version to an another one.
- Seems like there is no way to fully automate upgrade (as it was with JAR version) and it's required to go through configuration wizard each time.
- During upgrade select previous release directory as a source (or restore from backup).
- Proper way to upgrade from JAR version is to create backup, stop service, (re)move `youtrack_home_dir`, install YouTrack from scratch and restore backup.

## Requirements

Zip or unzip should be installed on target host.

JDK is not required because of embedded into archive version is used.

## Role Variables

| Variable | Description | Default value |
|----------|-------------|---------------|
| youtrack_version | YourTrack version to install | `2023.2.20316` |
| youtrack_create_user | Create dedicated user otherwise user should exist | `true` |
| youtrack_user | User to run YouTrack service | `youtrack` |
| youtrack_group | Group for YouTrack user | `{{ youtrack_user }}` |
| youtrack_home_dir | Home directory for YouTrack user | `/home/{{ youtrack_user }}` |
| youtrack_base_dir | Location of the symbolic link for the latest version of youtrack installed | `{{ youtrack_home_dir }}/youtrack` |
| youtrack_data_dir | YouTrack data directory | `{{ youtrack_home_dir }}/data` |
| youtrack_logs_dir | YouTrack logs directory | `{{ youtrack_home_dir }}/logs` |
| youtrack_backups_dir | YouTrack backups directory | `{{ youtrack_home_dir }}/backups` |
| youtrack_releases_dir | Directory to extract YouTrack ZIP atchive | `{{ youtrack_home_dir }}/releases` |
| youtrack_restore_backup | Restore YourTrack from given backup file, all data will be removed, use this with caution | `false` |
| youtrack_restore_backup_file | Backup file to restore | N/A |
| youtrack_options | YouTrack options, check [this](https://www.jetbrains.com/help/youtrack/server/Configure-JVM-Options.html) and [this](https://www.jetbrains.com/help/youtrack/server/YouTrack-Java-Start-Parameters.html) for the completed list | see `defaults/main.yml` |

## Example Playbook

```
- name: install youtrack
  hosts: all
  vars:
    youtrack_logs_dir: "/var/log/youtrack"
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
