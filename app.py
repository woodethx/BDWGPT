from app import create_app, db
from app.models import Order, System, ChecklistItem

app = create_app()


@app.cli.command('initdb')
def initdb():
    db.create_all()
    print('Database initialized.')


if __name__ == '__main__':
    app.run(debug=True)
