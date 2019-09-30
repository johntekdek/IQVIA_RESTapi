from flask import url_for


class TestPage:
    def test_home_page(self, client):
        """Home page should return 200"""
        response = client.get('/contacts')
        assert response.status_code == 200


class TestContact:
    def test_contacts(self,client):
        response = client.get(url_for("contact.contacts"))
        assert response.status_code == 200
        assert 'john' in response.get_data(as_text=True)
