import requests

if __name__ == "__main__":
    r = requests.post('http://localhost:5000/student/Lisa', data={})
    print r.text

    r = requests.get('http://localhost:5000/student/Lisa')
    print r.text
