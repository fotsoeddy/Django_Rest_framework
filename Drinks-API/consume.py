import requests


def get_drinks():
    response = requests.get('http://localhost:8000/drinks/')
    return response.json()

def create_drink(name, description, price):
    response = requests.post('http://localhost:8000/drinks/', json={'name': name, 'description': description, 'price': price})
    return response.json()

def update_drink(drink_id, name=None, description=None, price=None):
    data = {}
    if name:
        data['name'] = name
        if description:
            data['description'] = description
            if price:
                data['price'] = price
                response = requests.put(f'http://localhost:8000/drinks/{drink_id}/', json=data)
                return response.json()
            response = requests.put(f'http://localhost:8000/drinks/{drink_id}/', json={'name': name})
            return response.json()
        if price:
            data['price'] = price
            response = requests.put(f'http://localhost:8000/drinks/{drink_id}/', json=data)
            return response.json()
        
        response = requests.put(f'http://localhost:8000/drinks/{drink_id}/', json={'description': description})
        return response.json()
    if description:
        data['description'] = description
        if price:
            data['price'] = price
            response = requests.put(f'http://localhost:8000/drinks/{drink_id}/', json=data)
            return response.json()
        
        response = requests.put(f'http://localhost:8000/drinks/{drink_id}/', json={'name': name})
        
        return response.json()
    if price:
        data['price'] = price
        response = requests.put(f'http://localhost:8000/drinks/{drink_id}/', json=data)
        return response.json()
    response = requests.get(f'http://localhost:8000/drinks/{drink_id}/')
    return response.json()

def delete_drink(drink_id):
    response = requests.delete(f'http://localhost:8000/drinks/{drink_id}/')
    return response.status_code == 204

if __name__ == "__main__":
    print(get_drinks())
    print(create_drink('New Drink', 'This is a new drink', 5.99))
    print(update_drink(1, name='Updated Drink', description='This is an updated drink', price=6.99))
    print(delete_drink(1))
