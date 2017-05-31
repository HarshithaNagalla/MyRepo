import pytest

@pytest.mark.django_db

class Test_names:

    def test_get_name(self, client):
	response = client.get('/get_name/')
	assert response.status_code == 200

    def test_viewNames(self, client):
        response = client.get('/viewNames/')
        assert response.status_code == 200

