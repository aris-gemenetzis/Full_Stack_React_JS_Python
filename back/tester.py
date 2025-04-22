import requests


print(requests.get('http://localhost:8000/forms/0').json())


print(
    requests.post(
        "http://localhost:8000/forms/add",
        json={
            "company": "test_company", 
            "revenue": 3, 
            "costs": 2,
            "id": 1,
            }
    ).json())

print(
    requests.put(
        "http://localhost:8000/forms/1",
        json={
            "company": "new_name", 
            "revenue": 10, 
            "costs": 29,
            "id": 1,
            }
    ).json())


print(requests.delete("http://localhost:8000/forms/1").json())


print(
    requests.put(
        "http://localhost:8000/forms/0",
        json={
            "company": "new_company", 
            "revenue": 1, 
            "costs": 0,
            "id": 0,
            }
    ).json())

print(requests.get("http://localhost:8000/forms/0").json())
