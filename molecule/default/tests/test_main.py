def test_user(host):
    user = host.user('youtrack')
    assert user.exists
    assert user.group == 'youtrack'


def test_directory_symlink(host):
    directory = host.file('/home/youtrack/youtrack')
    assert directory.is_symlink
    linked_to = host.file(directory.linked_to)
    assert linked_to.is_directory
    assert linked_to.mode == 0o640
    assert linked_to.user == 'youtrack'
    assert linked_to.group == 'youtrack'


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
