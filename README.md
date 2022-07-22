# YouTrack ansible role

Role to install Jetbrains YouTrack project management platform.

YouTrack is installed from JAR file by process is described [here](https://www.jetbrains.com/help/youtrack/server/Install-YouTrack-JAR-as-Service-Linux.html).

## Requirements

JRE version greater than 11 should be installed.

## Role Variables

TBD

## Dependencies

TBD

## Example Playbook

TBD

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

## Author Information

TBD