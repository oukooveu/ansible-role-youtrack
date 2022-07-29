def test_user(host):
    user = host.user('youtrack')
    assert user.exists
    assert user.group == 'youtrack'


def test_file_jar(host):
    link = host.file('/home/youtrack/youtrack.jar')
    assert link.exists
    assert link.is_symlink
    jar = host.file(link.linked_to)
    assert jar.is_file
    assert jar.mode == 0o640
    assert jar.user == 'youtrack'
    assert jar.group == 'youtrack'


def test_file_conf(host):
    file = host.file('/home/youtrack/teamsysdata/conf/youtrack.jvmoptions')
    assert file.exists
    assert file.is_file
    assert file.contains('^-Ddisable.configuration.wizard.on.clean.install=False$')


def test_service(host):
    service = host.service('youtrack')
    assert service.is_running
    assert service.is_enabled


def test_port(host):
    socket = host.socket("tcp://0.0.0.0:8080")
    assert socket.is_listening
