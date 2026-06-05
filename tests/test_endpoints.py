def test_get_activities_returns_success_and_activity_map(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(data, dict)
    assert expected_activity in data


def test_get_activities_includes_participants_list(client):
    # Arrange
    activity_name = "Programming Class"

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert "participants" in data[activity_name]
    assert isinstance(data[activity_name]["participants"], list)