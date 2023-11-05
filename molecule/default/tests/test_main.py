def test_user(host):
    user = host.user('youtrack')
    assert user.exists
    assert user.group == 'youtrack'


def test_release(host):
    link = host.file('/home/youtrack/youtrack')
    assert link.exists
    assert link.is_symlink
    target = host.file(link.linked_to)
    assert target.is_directory
    assert target.mode == 0o750
    assert target.user == 'youtrack'
    assert target.group == 'youtrack'


def test_service(host):
    service = host.service('youtrack')
    assert service.is_running
    assert service.is_enabled


def test_port(host):
    socket = host.socket("tcp://0.0.0.0:8080")
    assert socket.is_listening
