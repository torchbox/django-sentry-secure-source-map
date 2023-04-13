def test_get_sourcemap(client):
    response = client.get("/static/index.js.map")
    assert response.status_code == 403


def test_get_non_static_url(client):
    response = client.get("/somewhere-else/world.map")
    assert response.status_code == 404


def test_get_static_file(client):
    response = client.get("/static/index.js")
    assert response.status_code == 200


def test_get_sourcemap_with_token(client, settings):
    response = client.get(
        "/static/index.js.map", HTTP_X_SENTRY_TOKEN=settings.SENTRY_SECURITY_TOKEN
    )
    assert response.status_code == 200


def test_no_protected_paths(client, settings):
    settings.SENTRY_PROTECTED_PATHS = []

    response = client.get("/static/index.js")
    assert response.status_code == 200
