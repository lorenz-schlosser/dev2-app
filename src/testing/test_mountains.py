from dev2il_devops_app.mountains import highest_mountain

def test_highest_mountain():
    mountains = [
        {'name': 'K2', 'height': 8611},
        {'name': 'Kilimanjaro', 'height': 5895},
        {'name': 'Everest', 'height': 8848}
    ]
    assert highest_mountain(mountains) == {''
        'name': 'Everest', 'height': 8848
    }