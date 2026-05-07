from app import create_app

app = create_app()

with app.test_client() as c:
    c.get('/greet?name=Pipeline')
    c.post('/calculate', json={'a': 5, 'b': 3})
    c.post('/todos', json={'task': 'Test task'})

print('Log file generated!')
